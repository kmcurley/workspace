import json
import os

# Load pending tickets
with open('pending-ticket.json', 'r') as f:
    new_tickets = json.load(f).get('new_tickets', [])

# Load existing ticket list
with open('tic-id.json', 'r') as f:
    ticket_list = json.load(f)

# Add new tickets if they aren't already in the list
added = []
for ticket in new_tickets:
    if ticket not in ticket_list:
        ticket_list.append(ticket)
        added.append(ticket)

# Save updated ticket list if changes were made
if added:
    with open('tic-id.json', 'w') as f:
        json.dump(ticket_list, f, indent=2)
    print(f"Added new tickets: {added}")
else:
    print("No new tickets to add.")
