def loading_bar(loaded_percentage: int):
    percentage_sing = "%" * (loaded_percentage // 10)
    dot_sing = "." * (10 - (loaded_percentage // 10))

    if loaded_percentage < 100:
        print(f"{loaded_percentage}% [{percentage_sing}{dot_sing}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{percentage_sing}{dot_sing}]")


loaded_process = int(input())
loading_bar(loaded_process)