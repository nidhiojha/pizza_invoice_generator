class InvoiceGeneratingSystem:
	def __init__(self):
		pass


	def get_personal_details(self):
		detail_dict = {}

		detail_dict["name"] = input("Please enter customer name: ")
		detail_dict["surname"] = input("Please enter customer sur-name: ")
		detail_dict["age"] = input("Please enter customer age: ")

		return detail_dict 

	def get_entry_ticket_price(self, age):
		if age < 4:
			return 200

		elif age >= 4 and age <18:
			return 350

		else:
			return 450

	def get_details_of_pizza(self):
		veg_toppings = ["Bell Pepper", "Mushrooms", "Goat Cheese", "Tofu"]
		non_veg_toppings = ["Pepproni", "Ham", "Salami", "Salmon"]
		ingridients_list = ["sauce", "mozzarella"]
		result_dict = {}

		type_of_pizza = input("Please enter veg/non-veg pizza: ").lower()


		if type_of_pizza == "veg":
			print("Available {} pizza ingridents are: {}".format(type_of_pizza, veg_toppings))
			count_ingridents = input("Please enter number of {} ingridents upto count 2: ". format(type_of_pizza))

			if int(count_ingridents) > 2 or int(count_ingridents) < 0:
				return ("Invalid number of ingridents. Please fill your details again.")

				
			else:
				elem= 0
				while elem < int(count_ingridents):
					ingridients = input("Enter {} ingridents: ". format(elem+1))
					temp_list = [items.lower() for items in veg_toppings]
					if ingridients.lower() in temp_list:
						ingridients_list.append(ingridients)
						elem+=1
					else:
						print("please choose among available ingridents")
				total_ingridents_price = int(count_ingridents) * 190

		else:
			print("Available {} pizza ingridents are: {}".format(type_of_pizza, non_veg_toppings))
			count_ingridents = input("Please enter number of {} ingridents upto count 2: ". format(type_of_pizza))
			if int(count_ingridents) > 2 or int(count_ingridents) < 0:
				print("Invalid number of ingridents")
				return
			else:
				elem = 0
				while elem < int(count_ingridents):
					ingridients = input("Enter {} ingridents: ".format(elem+1))
					temp_list = [items.lower() for items in non_veg_toppings]
					if ingridients.lower() in temp_list:
						ingridients_list.append(ingridients)
						elem+=1

					else:
						print("please choose among available ingridents")
				total_ingridents_price = int(count_ingridents) * 245

		result_dict["price"] = total_ingridents_price
		result_dict["ingridients"] = ingridients_list
		result_dict["pizza_type"] = type_of_pizza.lower()
		# print(ingridients_list)
		return result_dict

			
	def get_order_invoice(self):

		customer_personal_details = self.get_personal_details()

		age = int(customer_personal_details["age"])
		entry_ticket_price = int(self.get_entry_ticket_price(age))
		print("\n")

		count_pizzas = input("Enter number of pizzas to be order: ")

		total_cost = 0
		price_per_pizza = 0

		final_check_out = []

		elem = 0
		while elem < int(count_pizzas):
			print("\n")

			print("Enter {} Pizza Details: \n".format(elem+1))
		
			pizza_details = self.get_details_of_pizza()
			price_of_pizza = pizza_details["price"]
			price_per_pizza += price_of_pizza 
			final_check_out.append(pizza_details)
			elem +=1
			print("\n")

		print(" Please check final summary of order")
		print("\n")
		count = 0
		for elem in final_check_out:
			
			print("******* order {} details ********".format(count+1))
			print("Pizza Type: {}".format(elem["pizza_type"]))
			print("Ingridients: {}".format(elem["ingridients"]))
			print("Price: {} INR".format(elem["price"]))
			print("\n")

			count +=1

		print("Entry ticket price: {} INR".format(entry_ticket_price))
		print("Cart total price: {} INR ".format(price_per_pizza))
		total_cost = price_per_pizza + 0.18 * (price_per_pizza + entry_ticket_price)

		print("Amount Payable (including {}% GST): {} INR ".format(str(18), total_cost))
		print("\n")
		print("Thank you {} for your order!".format(customer_personal_details["name"]))





if __name__ == '__main__':
	ob = InvoiceGeneratingSystem()
	ob.get_order_invoice()
