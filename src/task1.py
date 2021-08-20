"""модель оплаты комунальных счетов"""


class PaymentWaterSupplySewerage:
    """Расчет водоснабжения и водоотведения.

    Расчет стоимости услуг водонакала по обеспечению населения холодным и
    горячим водоснабжением, а так же водоотведением.

    Args:
    PREFERENTIAL_PRICE_COLDWATER -- льготная цена за 1 метр кубический
    воды в руб.
    FULL_PRICE_COLDWATER -- полная цена за 1 метр кубический воды в руб.
    NORM_WATER_PERSON -- норма объема воды на одного жителя за месяц.
    PRICE_HOTWATER -- полная цена за подогрев 1 метра кубического воды в руб.
    PREFERENTIAL_PRICE_SEWERAGE -- льготная цена за отведение 1 метра
    кубического сточной воды в руб.
    FULL_PRICE_SEWERAGE -- полная цена за отведение 1 метра кубического
    сточной воды в руб.
    """
    PREFERENTIAL_PRICE_COLDWATER = 0.92
    FULL_PRICE_COLDWATER = 1.1
    NORM_WATER_PERSON = 4
    PRICE_HOTWATER = 1.65
    PREFERENTIAL_PRICE_SEWERAGE = 0.59
    FULL_PRICE_SEWERAGE = 0.63

    def __init__(self, number_of_people, hotwater1, hotwater2, coldwater1,
                 coldwater2):
        """Args:

        number_of_people -- количество людей зарегистрированных в квартире,
        hotwater1 -- показания счетчика горячей воды за прошлый месяц,
        hotwater2 -- показания счетчика горячей воды за текущий месяц,
        coldwater1 -- показания счетчика холодной воды за прошлый месяц,
        coldwater2 -- показания счетчика горячей воды за текущий месяц,
        """
        self.hotwater1 = hotwater1
        self.hotwater2 = hotwater2
        self.coldwater1 = coldwater1
        self.coldwater2 = coldwater2
        self.number_of_people = number_of_people
        self.pay_coldwater = None
        self.pay_hotwater = None
        self.pay_sewers = None
        # расчет объма воды использованного за месяц
        self.water_volume = (self.coldwater2 - self.coldwater1) + \
                            (self.hotwater2 - self.hotwater1)
        # расчет максимального объема воды за месяц, который могут использовать
        # жильцы по льготной цене
        self.preferential_volume =\
            PaymentWaterSupplySewerage.NORM_WATER_PERSON * \
            self.number_of_people

    def payment_coldwater(self):
        """Расчет стоимости за холодное водоснабжение.

        pay_coldwater -- стоимость холодного водоснабжения в руб.
        """

        if self.water_volume < self.preferential_volume:
            pay_coldwater = \
                self.water_volume * \
                PaymentWaterSupplySewerage.PREFERENTIAL_PRICE_COLDWATER
            pay_coldwater = round(pay_coldwater, 2)
        else:
            pay_coldwater = self.preferential_volume * \
                PaymentWaterSupplySewerage.PREFERENTIAL_PRICE_COLDWATER + \
                (self.water_volume - self.preferential_volume) * \
                PaymentWaterSupplySewerage.FULL_PRICE_COLDWATER
            pay_coldwater = round(pay_coldwater, 2)
        self.pay_coldwater = pay_coldwater
        print(f"Плата за холодное водоснабжение: {pay_coldwater} руб.")

    def payment_hotwater(self):
        """Расчет стоимости за холодное водоснабжение.

        pay_hotwater -- стоимость горячего водоснабжения в руб.
        """
        pay_hotwater = (self.hotwater2 - self.hotwater1) * \
            PaymentWaterSupplySewerage.PRICE_HOTWATER
        pay_hotwater = round(pay_hotwater, 2)
        self.pay_hotwater = pay_hotwater
        print(f"Плата за горячее водоснабжение: {pay_hotwater} руб.")

    def paymant_sewerage(self):
        """Расчет стоимости водоотведения.

        pay_sewers -- стоимость водоотведения в руб.
        """
        if self.water_volume < self.preferential_volume:
            pay_sewers = self.water_volume * \
                PaymentWaterSupplySewerage.PREFERENTIAL_PRICE_SEWERAGE
            pay_sewers = round(pay_sewers, 2)
        else:
            pay_sewers = self.preferential_volume * \
                PaymentWaterSupplySewerage.PREFERENTIAL_PRICE_SEWERAGE + \
                (self.water_volume - self.preferential_volume) * \
                PaymentWaterSupplySewerage.FULL_PRICE_SEWERAGE
            pay_sewers = round(pay_sewers, 2)
        self.pay_sewers = pay_sewers
        print(f"Плата за водоотведение: {pay_sewers} руб.")

    def all_payment_water(self):
        """Расчет общей стоимости услуг водоканала.

        all_pay_water_sewers -- стоимость водоснабжения и водоотведения
        в руб.
        """
        all_pay_water_sewers = self.pay_coldwater + self.pay_hotwater + \
            self.pay_sewers
        all_pay_water_sewers = round(all_pay_water_sewers, 2)
        print(f"Плата за услуги водоканала: {all_pay_water_sewers} руб.")


class PaymentGasSupple:
    """Расчет стоимости услуг газоснабжения населения.

    Args:
    PRICE_GAS -- цена за 1 метр кубический газа в руб.
    """
    PRICE_GAS = 0.5082

    def __init__(self, meter1_gas, meter2_gas):
        """Args:

        meter1_gas -- показания счетчика газаснабжения за прошлый месяц,
        meter2_gas -- показания счетчика газаснабжения за текущий месяц.
        """
        self.meter1_gas = meter1_gas
        self.meter2_gas = meter2_gas

    def payment_gas(self):
        """Расчет стоимости газаснабжения.

        pay_gas -- стоимость газаснабжения в руб.
        """

        pay_gas = (self.meter2_gas - self.meter1_gas) * \
            PaymentGasSupple.PRICE_GAS
        pay_gas = round(pay_gas, 2)
        print(f"Плата за газоснабжение: {pay_gas} руб.")


class PaymentElectricity:
    """Расчет стоимости использования электроэнергии населением.

    Args:
    PRICE_ELECTRICITY -- цена за 1 кВт*ч в руб.
    """
    PRICE_ELECTRICITY = 0.23

    def __init__(self, meter1_elecric, meter2_elecric):
        """Args:

        meter1_elecric -- показания счетчика электроэнергии за прошлый месяц,
        meter2_elecric -- показания счетчика электроэнергии за текущий месяц.
        """
        self.meter1_elecric = meter1_elecric
        self.meter2_elecric = meter2_elecric

    def payment_electricity(self):
        """Расчет стоимости использования электроэнергии.

        pay_gas -- стоимость электроэнергии в руб.
        """

        pay_elec = (self.meter2_elecric - self.meter1_elecric) * \
            PaymentElectricity.PRICE_ELECTRICITY
        pay_elec = round(pay_elec, 2)
        print(f"Плата за электроэнергию: {pay_elec} руб.")


class CommunalPayments():
    """Оплата коммунальных платежуй"""

    def __init__(self, number_of_people, hotwater1, hotwater2, coldwater1,
                 coldwater2, meter1_gas, meter2_gas, meter1_elecric,
                 meter2_elecric):
        self.water = PaymentWaterSupplySewerage(number_of_people, hotwater1,
                        hotwater2, coldwater1, coldwater2)
        self.gas = PaymentGasSupple(meter1_gas, meter2_gas)
        self.elec = PaymentElectricity(meter1_elecric, meter2_elecric)

    def run(self):
        """Вывод общей информации по всем платежам. """

        self.water.payment_coldwater()
        self.water.payment_hotwater()
        self.water.paymant_sewerage()
        self.water.all_payment_water()
        self.gas.payment_gas()
        self.elec.payment_electricity()


all = CommunalPayments(2, 20, 25, 10, 15, 12, 18, 12, 67)
all.run()
