import json
import os

# Load pending ticket
with open('pending-ticket.json', 'r') as f:
    new_ticket = json.load(f)['new_ticket']

# Load existing ticket list
with open('workspace/tic-id.json', 'r') as f:
    ticket_list = json.load(f)

# Update if new
if new_ticket not in ticket_list:
    ticket_list.append(new_ticket)
    with open('workspace/tic-id.json', 'w') as f:
        json.dump(ticket_list, f, indent=2)
    print(f"Added new ticket: {new_ticket}")
else:
    print("Ticket already exists. No update needed.")
