def sort_contacts(contacts):
    contacts_list = list(contacts.items())
    contacts_list.sort()
    return_list = []
    for (k, v) in contacts_list:        
        return_list.append((k,)+v)
    return return_list
