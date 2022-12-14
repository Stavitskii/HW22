from classes.shop import Shop
from classes.store import Store
from items import store_items, shop_items

from classes.request import Request

store = Store()
shop = Shop()
store.items = store_items
shop.items = shop_items


def main():
    print('Привет! Программа симулирует движение товаров между складом и магазином\n'
          '\nДля отправки товаров нужно ввести сообщение\n'
          'Формат: Доставить [кол-во] [наименование] из [откуда] в [куда]\n'
          'Пример: Доставить 2 хомяк из склад в магазин\n'
          '\nДля остановки программы в любой момент введите "стоп"\n')
    while True:
        user_input = input("Введите запрос: ")

        if user_input == "стоп":
            break

        request = Request(user_input)

        if request.from_ == "склад":
            req_from = store
            req_to = shop
            if request.product in req_from.items:
                print(f"Нужный товар есть в пункте \"{request.from_}\".")
            else:
                print(f"В пункте {request.from_} нет такого товара.")
                continue

            if req_from.items[request.product] >= request.amount:
                print(f"Нужное количество есть в пункте \"{request.from_}\".")
            else:
                print(f"В пункте {request.from_} не хватает {request.amount - req_from.items[request.product]}.")
                continue

            if req_to.get_free_space >= request.amount:
                print(f"В пункте \"{request.to}\" достаточно места.")
            else:
                print(f"В пункте {request.to} не хватает {request.amount - req_to.get_free_space}.")
                continue

            if request.to == "магазин" and shop.get_unique_items_count == 5 and request.product not in shop.items:
                print("В магазине достаточно уникальных значений.")
                continue

            req_from.remove(request.product, request.amount)
            print(f"Курьер забрал {request.amount} {request.product} из пункта {request.from_}.")
            print(f"Курьер везет {request.amount} {request.product} из пункта {request.from_} в пункт {request.to}.")
            req_to.add(request.product, request.amount)
            print(f"Курьер доставил {request.amount} {request.product} в пункт {request.to}.")

        print("=" * 30)
        print("На складе:")
        for title, count in store.items.items():
            print(f"{title}: {count}.")
        print(f"Свободного места {store.get_free_space}.")

        print("=" * 30)
        print("В магазине:")
        for title, count in shop.items.items():
            print(f"{title}: {count}.")
        print(f"Свободного места {shop.get_free_space}.")
        print("=" * 30)


if __name__ == "__main__":
    main()
