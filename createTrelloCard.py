# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

def GetCardID():
    cardID = input("\nEnter a unique 5 digit identifier for the card: ")
    return cardID

def GetCardName():
    cardName = input("Enter a name for the card: ")
    return cardName

def CreateCard(cardTitle, cardDescription):
    # initialize url
    url = "https://api.trello.com/1/cards"

    # initialize headers
    headers = {
        "Accept": "application/json"
    }

    # initialize query parameters
    query = {
        'idList': 'idList',
        'key': 'key',
        'token': 'token',
        'name': cardTitle,
        'desc': cardDescription,
    }

    # make the request
    requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

def main():
  # initialize card metadata
  cardID = GetCardID()
  cardName = GetCardName()
  cardTitle = "[" + cardID + "] " + cardName # EX) [12345] Test123
  cardDescription = "# " + str(cardName) + "\n\n---\n\n## Summary\n\nbrief summary of the changes that need to be made\n\n## Rationale\n\nWhy was the card created\n\n## Action Items\n\n- high level bullets to implement the changes"
  
  # create a new card using the /cards API
  CreateCard(cardTitle, cardDescription)

  print("\nDone!\n")

if __name__ == "__main__":
    main()
