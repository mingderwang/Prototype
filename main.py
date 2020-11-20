from utils.prototype import A


class App:
    def main():
        a = A(1)
 
        b = A(100)
        b.printSize()

        c = a.clone()
        c.printSize()

        print


App.main()