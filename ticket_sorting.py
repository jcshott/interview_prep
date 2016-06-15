"""
code question from Infer

Ticket Sorting
ticket = (SRC, DEST)
input = [(SFO, LAX), (JFK, SEA), (SEA, SFO)]
sorted = [(JFK, SEA), (SEA, SFO), (SFO, LAX)]
"""

# list of inputs
# which dest. doesn't have a matching src = ending destination
# src that doesn't a destination is our starting src.
# match tup[1] tup[0]

def sort_tickets(tickets):
    # key src: value=dest
    ticket_dict = {}
    city_count = {}

    for src, dest in tickets:
        ticket_dict[src] = dest #SFO: LAX; JFK:SEA; SEA:SFO
        city_count[src] = city_count.get(src, 0) + 1
        count_count[dest] = city_count.get(dest, 0) + 1

    # ticket_dict = {sfo: lax, jfk: sea, sea: sfo}

    start_point = None #JFK

    for key, val in city_count:
        if val == 1 and key in ticket_dict:
            start_point = key


    trip_array = [(start_point, ticket_dict[start_point]) ]
    #[(JFK, SEA)]
    while len(trip_array) < len(tickets):
        curr_dest = trip_array[-1][1] # SEA; SFO
        trip_array.append((curr_dest, ticket_dict[curr_dest)] # (SEA, SFO) (SFO, LAX)

    return trip_array
