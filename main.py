from utils.prototype import A


class App:
    def main():
        a = A(1)
        for i in range(2, 10):
            temp = a.clone()
            temp.setSize(i)
            temp.printSize()


App.main()