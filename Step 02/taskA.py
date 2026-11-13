# header comment

slices_per_pizza = 8
pizza_price = 12.99
slice_price = 2.25

# input
host_name = input("Your name: ")
guest_text = input("How many guests: ")
slice_text = input("Slice per person: ")


guest_number = int(guest_text)
slice_number = int(slice_text)
total_slices = guest_number * slice_number
whole_pizzas = total_slices // slices_per_pizza
extra_slices = total_slices % slices_per_pizza
total_cost = whole_pizzas * pizza_price + extra_slices * slice_price
cost_per_person = total_cost // guest_number
total_slices_text = str(total_slices)
whole_pizzas_text = str(whole_pizzas)
extra_slices_text = str(extra_slices)
total_cost_text = str(total_cost)
cost_per_person_text = str(cost_per_person)

# output
print("=== Pizza Plan for " + host_name + " Party ===")
print("Slices needed:    " + total_slices_text )
print("Whole pizzas:     " + whole_pizzas_text )
print("Extra slices      " + extra_slices_text )
print("Total cost:       " + total_cost_text )
print("Cost per person:  " + cost_per_person_text )
