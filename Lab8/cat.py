class Cat:
    def __init__(self, Name, Breed):
        self.Name = Name
        self.Breed = Breed

    def meow(self):
        print(f"{self.Name} meows at you!")

    def hides(self):
        print(f"{self.Name} hides from you..")

cat_names = ["Ufo", "Hoshi", "Sora", "Okami", "Memmi"]

# Create cats
cats = []
for i in range(5):
    cat:Cat = Cat(cat_names[i], "Ragdoll")
    cats.append(cat)

#Loop through them
for cat in cats:
    cat.meow()
    cat.hides()
