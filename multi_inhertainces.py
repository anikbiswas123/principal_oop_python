# class Car:
#     def go(self):
#         print("Going")
#
#
# class flyable:
#     def fly(self):
#         print("flyable")
#
#
# class flyingCar(Car, flyable):
#     def stop(self):
#         print("stod")
#
#
# fly = flyingCar()
#
# fly.go()
# fly.fly()
# fly.stop()


class Car:
    pass
    # def start(self):
    #     print("start the Car")

    # def go(self):
    #     print("Going")


class flyable:
    def start(self):
        print("starte the flyable objects")

    # def fly(self):
    #     print("flying")

    def go(self):
        print("Going")


class FlyingCar(Car,flyable):
    def start(self):
        super().start()
        super().go()



Fly=FlyingCar()
Fly.start()