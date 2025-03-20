def input_error(func):
  def inner(*args, **kwargs):
      try:
        return func(*args, **kwargs)
      except ValueError:
         return "Error: Please include name and phone number"
      except KeyError:
         print("Invalid command.")
        #  return 
      except IndexError:
         print("The list is currently empty")
        #  return 
  return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args

    if len(args) < 2:
      raise ValueError
    elif args[0].lower() in contacts.keys():
      return "Contact already exists. If you want to change the details then use the change function"
    else:
      contacts[name] = phone
      return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args

    if len(args) < 2:
      raise ValueError
    else:
      contacts[name] = phone
      return f"Contact {name} changed to {phone}"

def show_phone(args, contacts):
    name = args

    if len(args) < 1:
      print("Error: you forgot to give the name of the contact")
    else:
      print(contacts[name])
      return f"{contacts[name]}"

@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            if len(contacts) == 0:
              raise IndexError
            else:
              print(contacts)
        else:
            raise KeyError

if __name__ == "__main__":
    main()