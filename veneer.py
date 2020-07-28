class Art:
    def __init__(self,artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{}. {}. {}, {}. Owned by {}, {}.".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)

class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self,new_listing):
        self.listings.append(new_listing)

    def remove_listing(self,bad_listing):
        self.listings.remove(bad_listing)

    def show_listings(self):
        for x in self.listings:
            print(x)
        print()

class Client:
    def __init__(self,name,location,is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum


    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            x = Listing(artwork,price,self)
            veneer.add_listing(x)

    def buy_artwork(self,artwork):
        if artwork.owner != self and artwork in veneer.listings:
            pass

class Listing:
    def __init__(self,art,price,seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "{} for ${}".format(self.art.title, self.price)

veneer = Marketplace()

edytta = Client("Edytta Halpirt","Private Collection",False)
moma = Client("The MOMA","New York",True)

girl_with_madolin = Art("Picasso, Pablo",'"Girl with madolin"',"oil on canvas",1910,edytta)
#print(girl_with_madolin)

edytta.sell_artwork(girl_with_madolin,6000000)
veneer.show_listings()

moma.buy_artwork(girl_with_madolin)

