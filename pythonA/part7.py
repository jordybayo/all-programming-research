# template

from string import Template



def Main():

    cart = []

    cart.append(dict(item="coka", price=650, qte=1))
    cart.append(dict(item="poisson", price=1000, qte=2))
    cart.append(dict(item="poulet", price=1500, qte=4))

    t = Template("$qte x $item = $$price")
    total = 0
    print("Cart: ")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
    print("Total : " + str(total))

if __name__ == '__main__':
    Main()
