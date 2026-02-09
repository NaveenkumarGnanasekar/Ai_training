n = int(input("enter number of crash reports: "))
lst = []

for _ in range(n):
    version = input("App version: ")
    device = input("Device: ")
    severity = input("Severity: ")
    lst.append({"app_version": version, "device": device, "severity": severity})
high_reports = [r for r in lst if r["severity"] == "HIGH"]
version_count = {}
for r in lst:
    v = r["app_version"]
    version_count[v] = version_count.get(v, 0) + 1
print("HIGH severity reports:", high_reports)
print("crash count per app version:", version_count)
