import requests

API_BASE_URL = "http://localhost:8080/products"


class ProductAPI:
    def __init__(self, requests_module=requests):
        self.requests_module = requests_module

    def make_request(self, method, endpoint, data=None):
        url = f"{API_BASE_URL}/{endpoint}"
        headers = {"Content-Type": "application/json"}

        if method.lower() == "get":
            response = self.requests_module.get(url)
        elif method.lower() == "post":
            response = self.requests_module.post(
                url, json=data, headers=headers)
        elif method.lower() == "put":
            response = self.requests_module.put(
                url, json=data, headers=headers)
        elif method.lower() == "delete":
            response = self.requests_module.delete(url)

        return response

    def get_all_products(self):
        response = self.make_request("GET", "")
        if response.status_code == 200:
            response_data = response.json()
            for product in response_data:
                print("Product Name:", product["productName"])
                print("Product price:", product["price"])
                print("Code :", product['productCode'])
        else:
            print(
                f"Failed to retrieve products. Status code: {response.status_code}")

    def get_product(self, product_id):
        response = self.make_request("GET", product_id)
        if response.status_code == 200:
            response_data = response.json()
            print("Product found:")
            print(f"Product Name: {response_data['productName']}")
            print(f"Price: {response_data['price']}")
            print(f"Code: {response_data['productCode']}")
        else:
            print(
                f"Failed to retrieve product with ID {product_id}. Status code: {response.status_code}")

    def create_product(self, name, price, code):
        data = {
            "productName": name,
            "price": price,
            "productCode": code
        }
        response = self.make_request("POST", "", data)
        if response.status_code == 200:
            print("Product created successfully.")
        else:
            print(
                f"Failed to create product. Status code: {response.status_code}")

    def update_product(self, product_id, name, price, code):
        data = {
            "productName": name,
            "price": price,
            "productCode": code
        }
        response = self.make_request("PUT", product_id, data)
        if response.status_code == 200:
            print("Product updated successfully.")
        else:
            print(
                f"Failed to update product. Status code: {response.status_code}")

    def delete_product(self, product_id):
        response = self.make_request("DELETE", product_id)
        if response.status_code == 200:
            print("Product deleted successfully.")

        elif response.status_code == 404:
            print("Product not found.")

        else:
            print(
                f"Failed to delete product. Status code: {response.status_code}")


def main():
    print("Welcome to Product Management Console App")
    product_api = ProductAPI()

    while True:
        print("----------------------")
        print("\nActions:")
        print("1: Create product")
        print("2: Update product")
        print("3: Delete product")
        print("4: Get all products")
        print("5: Get product by ID")
        print("6: Close")
        print("----------------------")

        action = input("Enter action number: ")

        if action == "1":  # Create product
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            code = input("Enter product code: ")
            product_api.create_product(name, price, code)
        elif action == "2":  # Update product
            product_id = input("Enter product ID to update: ")
            name = input("Enter updated product name: ")
            price = float(input("Enter updated product price: "))
            code = input("Enter updated product code: ")
            product_api.update_product(product_id, name, price, code)
        elif action == "3":  # Delete product
            product_id = input("Enter product ID to delete: ")
            product_api.delete_product(product_id)
        elif action == "4":  # Get all products
            product_api.get_all_products()
        elif action == "5":  # Get product by ID
            product_id = input("Enter product ID to retrieve: ")
            product_api.get_product(product_id)
        elif action == "6":  # Close
            break
        else:
            print("Invalid action.")


if __name__ == "__main__":
    main()
