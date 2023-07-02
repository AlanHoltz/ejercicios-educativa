from utils.common import clear


def sort(names:list):

    names = format_names(names)
    
    names = sorted(names)

    return create_dict(names)


def format_names(names:list):       
    
    for i, full_name in enumerate(names):
        name = " ".join(full_name.split(" ")[:-1])
        surname = full_name.split(" ")[-1]
        names[i] = f"{surname}, {name}"

    return names


def create_dict(names:list):
    
    dict_names = {}

    for i in range(1,len(names) + 1):
        dict_names[i] = names[i - 1]

    return dict_names


def main():
    
    clear()

    names = ["Jacinta Flores", "Juan Carlos Feletti","Pedro Lugones", "Ana María Galíndez"]
    
    print(sort(names))


if __name__ == "__main__":
    main()