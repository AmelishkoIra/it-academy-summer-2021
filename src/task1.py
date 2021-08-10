"""Модель оплаты комунальных счетов"""


class Payment_water_supply_sewerage:
    """Расчет стоимости услуг водонакала по обеспечению населения холодным и
    горячим водоснабжением, а так же водоотведением
    """
    def __init__(self, number_of_people, hotwater1, hotwater2, coldwater1,
                 coldwater2):
        """Keyword arguments:
        number_of_people -- количество людей зарегистрированных в квартире,
        hotwater1 -- показания счетчика горячей воды за прошлый месяц,
        hotwater2 -- показания счетчика горячей воды за текущий месяц,
        coldwater1 -- показания счетчика холодной воды за прошлый месяц,
        coldwater2 -- показания счетчика горячей воды за текущий месяц,
        norm_water_per_person- норма объема воды на одного жителя за месяц
        """
        self.hotwater1 = hotwater1
        self.hotwater2 = hotwater2
        self.coldwater1 = coldwater1
        self.coldwater2 = coldwater2
        self.number_of_people = number_of_people
        self.norm_water_per_person = 4
        # расчет объма воды использованного за месяц
        self.water_volume = (self.coldwater2 - self.coldwater1) + \
                            (self.hotwater2 - self.hotwater1)
        # расчет максимального объема воды за месяц, который могут использовать
        # жильцы по льготной цене
        self.preferential_volume = self.norm_water_per_person * \
                                   self.number_of_people
    def payment_coldwater(self):
        """Расчет стоимости за холодное водоснабжение.

        preferential_price_coldwater -- льготная цена за 1 метр кубический воды
        в руб.
        full_price_coldwater -- полная цена за 1 метр кубический воды в руб.
        payment_coldwater -- стоимость холодного водоснабжения в руб.
        """

        preferential_price_coldwater = 0.92
        full_price_coldwater = 1.1
        global payment_coldwater
        if self.water_volume < self.preferential_volume:
            payment_coldwater = round(self.water_volume * \
                                      preferential_price_coldwater, 2)
        else:
            payment_coldwater = round(self.preferential_volume * \
                                      preferential_price_coldwater + \
                                      (self.water_volume - \
                                      self.preferential_volume) \
                                      * full_price_coldwater, 2)
        print(f"Плата за холодное водоснабжение: {payment_coldwater} руб.")


    def payment_hotwater(self):
        """Расчет стоимости за холодное водоснабжение.

        price_hotwater -- полная цена за подогрев 1 метра кубического воды
        в руб.
        payment_hotwater -- стоимость горячего водоснабжения в руб.
        """
        price_hotwater = 1.65
        global payment_hotwater
        payment_hotwater = round((self.hotwater2 - self.hotwater1) * \
                                 price_hotwater, 2)
        print(f"Плата за горячее водоснабжение: {payment_hotwater} руб.")


    def paymant_sewerage(self):
        """Расчет стоимости водоотведения.

        preferential_price_sewerage -- льготная цена за отведение 1 метра
        кубического сточной воды в руб.
        full_price_sewerage -- полная цена за отведение 1 метра кубического
        сточной воды в руб.
        payment_sewers -- стоимость водоотведения в руб.
        """

        preferential_price_sewerage = 0.59
        full_price_sewerage = 0.63
        global payment_sewers
        if self.water_volume < self.preferential_volume:
            payment_sewers = round(self.water_volume * \
                                   preferential_price_sewerage, 2)
        else:
            payment_sewers = round(self.preferential_volume * \
                                   preferential_price_sewerage + \
                                   (self.water_volume - \
                                   self.preferential_volume) * \
                                   full_price_sewerage, 2)
        print(f"Плата за водоотведение: {payment_sewers} руб.")


    def all_payment_water(self):
        """Расчет общей стоимости услуг водоканала.

        all_payment_water_sewers -- стоимость водоснабжения и водоотведения
        в руб.
        """

        all_payment_water_sewers = round(payment_coldwater + \
                                         payment_hotwater + payment_sewers, 2)
        print(f"Плата за услуги водоканала: {all_payment_water_sewers} руб.")


class Payment_gas_supple:
    """Расчет стоимости услуг газоснабжения населения."""


    def __init__(self, meter1_gas, meter2_gas):
        """
        Keyword arguments:
        meter1_gas -- показания счетчика газаснабжения за прошлый месяц,
        meter2_gas -- показания счетчика газаснабжения за текущий месяц.
        """
        self.meter1_gas = meter1_gas
        self.meter2_gas = meter2_gas


    def payment_gas(self):
        """Расчет стоимости газаснабжения.

        price_gas -- цена за 1 метр кубический газа в руб.
        payment_gas -- стоимость газаснабжения в руб.
        """
        price_gas = 0.5082
        payment_gas = round((self.meter2_gas - self.meter1_gas) * \
                            price_gas, 2)
        print(f"Плата за газоснабжение: {payment_gas} руб.")


class Payment_electricity:
    """Расчет стоимости использования электроэнергии населением."""


    def __init__(self, meter1_elecric, meter2_elecric):
        """
        Keyword arguments:
        meter1_elecric -- показания счетчика электроэнергии за прошлый месяц,
        meter2_elecric -- показания счетчика электроэнергии за текущий месяц.
        """
        self.meter1_elecric = meter1_elecric
        self.meter2_elecric = meter2_elecric


    def payment_electricity(self):
        """Расчет стоимости использования электроэнергии.

        price_electricity -- цена за 1 кВт*ч в руб.
        payment_gas -- стоимость электроэнергии в руб.
        """
        price_electricity = 0.23
        payment_elec = round((self.meter2_elecric - \
                              self.meter1_elecric) * price_electricity, 2)
        print(f"Плата за электроэнергию: {payment_elec} руб.")


water = Payment_water_supply_sewerage(2, 20, 25, 10, 15)
water.payment_coldwater()
water.payment_hotwater()
water.paymant_sewerage()
water.all_payment_water()
gas = Payment_gas_supple(12, 18)
gas.payment_gas()
elec = Payment_electricity(12, 67)
elec.payment_electricity()
