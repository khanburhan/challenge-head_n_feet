def headfeet():
    total_heads = 22
    total_feet = 72

    for i in range(22):

        people_head = total_heads - i
        people_feet = people_head * 2

        dog_head = total_heads - people_head
        dog_feet = total_feet - people_feet

        if ((people_head + dog_head == 22) and (people_feet + dog_feet == 72)):
            people = people_head
            dogs = dog_head

            if ((dogs * 4) + (people * 2) == 72):

                print("People: ", people, "\nDogs: ", dogs)


headfeet()
