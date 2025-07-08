from locust import HttpUser, task, between
import random
from utility import get_config

# Check environment variable first
locust_host = os.getenv("LOCUST_HOST")

if not locust_host:
    # fallback to config file
    locust_config = get_config("locust")
    locust_host = locust_config["host"]

print(f"Using Locust host → {locust_host}")

class DemoApiUser(HttpUser):
    wait_time = between(1, 3)
    host = locust_host

    @task
    def get_hello(self):
        self.client.get("/api/hello")

    @task
    def get_ping(self):
        self.client.get("/api/ping")

    @task
    def get_time(self):
        self.client.get("/api/time")

    @task
    def get_status(self):
        self.client.get("/api/status")

    @task
    def post_echo(self):
        payload = {
            "message": "Hello from Locust!",
            "number": random.randint(1, 100)
        }
        self.client.post("/api/echo", json=payload)

    @task
    def get_all_products(self):
        self.client.get("/api/products")

    @task
    def get_product_by_id(self):
        product_id = random.randint(1, 10)
        self.client.get(f"/api/products/{product_id}")

    @task
    def post_add_product(self):
        payload = {
            "name": f"Product-{random.randint(100,999)}",
            "price": random.uniform(10, 99),
            "description": "Demo product from Locust test"
        }
        self.client.post(f"/api/products", json=payload)

    @task
    def put_update_product(self):
        product_id = random.randint(1, 10)
        payload = {
            "name": f"UpdatedProduct-{random.randint(100,999)}",
            "price": random.uniform(20, 150),
            "description": "Updated description"
        }
        self.client.put(f"/api/products/{product_id}", json=payload)

    @task
    def delete_product(self):
        product_id = random.randint(1, 10)
        self.client.delete(f"/api/products/{product_id}")
