# scalytics_locust
Load test app developed using python to support scalytics (Locust)

## Why Locust?

Locust is an open-source load testing tool used to simulate thousands of concurrent users to assess how systems perform under stress. It is:

- **Python-based** – easy to write custom test scenarios.
- **Scalable** – supports distributed load generation across multiple machines.
- **Lightweight & fast** – suitable for frequent performance tests in CI/CD.

---

## How We Currently Use Locust

Across several client engagements, our teams have employed Locust to:

- Test API performance under increasing user loads.
- Identify scaling thresholds (e.g. pinpointing where systems hit CPU/memory bottlenecks).
- Compare response times under different test configurations.
- Validate infrastructure readiness before production go-lives.

---

## Installation

First, install Locust using pip:

```bash
pip install locust
```

```bash
pip install locust==2.22.0
```

```
setx LOCUST_PROFILE "my_profile"
```

```bash
locust -f locustfile.py
```


