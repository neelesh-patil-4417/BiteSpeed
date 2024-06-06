from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from django.db.models import Q

@api_view(['HEAD','GET'])
def home(request):
    return Response({"message":"/api/identify/ is the end point"})

@api_view(['HEAD','POST'])
def identify(request):
    email = request.data.get('email')
    phoneNumber = request.data.get('phoneNumber')

    # Find existing contacts
    contacts = Contact.objects.filter(
        Q(email=email) | Q(phoneNumber=phoneNumber))

    if contacts.exists():
        primary_contact = contacts.filter(linkPrecedence='primary')
        if len(primary_contact) > 1:
            multiple_primary_contacts = contacts.filter(
                Q(linkPrecedence='primary') & Q(phoneNumber=phoneNumber))

            for contact in multiple_primary_contacts:
                contact.linkPrecedence = 'secondary'
                contact.save()

        contacts = Contact.objects.filter(
            Q(email=email) | Q(phoneNumber=phoneNumber))
        primary_contact = contacts.filter(linkPrecedence='primary').first()
        print(contacts.values())
        primary_contact_id = primary_contact.id
        new_contact = Contact.objects.create(email=email,
                                             phoneNumber=phoneNumber,
                                             linkPrecedence='secondary',
                                             linkedId=primary_contact_id)
        contacts = Contact.objects.filter(linkedId=primary_contact_id)

        emails = set()
        phone_numbers = set()
        secondary_contact_ids = []

        for contact in contacts:
            if contact.email:
                emails.add(contact.email)
                print(emails)
            if contact.phoneNumber:
                phone_numbers.add(contact.phoneNumber)
                print(phone_numbers)
            if contact.id != primary_contact_id:
                secondary_contact_ids.append(contact.id)

        emails.add(primary_contact.email)
        phone_numbers.add(primary_contact.phoneNumber)

        response = {
            "contact": {
                "primaryContactId": primary_contact_id,
                "emails": list(emails),
                "phoneNumbers": list(phone_numbers),
                "secondaryContactIds": secondary_contact_ids
            }
        }
    else:
        new_contact = Contact.objects.create(email=email,
                                             phoneNumber=phoneNumber,
                                             linkPrecedence='primary')
        response = {
            "contact": {
                "primaryContactId": new_contact.id,
                "emails": [email] if email else [],
                "phoneNumbers": [phoneNumber] if phoneNumber else [],
                "secondaryContactIds": []
            }
        }

    return Response(response)
