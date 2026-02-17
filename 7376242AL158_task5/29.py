class Device:
    def __init__(self, name, current_version):
        self.name = name
        self.current_version = current_version

    def install_update(self, new_version):
        self.current_version = new_version
        print(f"{self.name} updated to version {self.current_version}")
class UpdateStrategy:
    def apply_update(self, device, new_version):
        pass
class ImmediateUpdate(UpdateStrategy):
    def apply_update(self, device, new_version):
        print(f"Applying immediate update to {device.name}")
        device.install_update(new_version)


class ScheduledUpdate(UpdateStrategy):
    def apply_update(self, device, new_version):
        print(f"Scheduling update for {device.name}")
        print("...Update scheduled...")
        device.install_update(new_version)

class ManualApprovalUpdate(UpdateStrategy):
    def apply_update(self, device, new_version):
        print(f"Waiting for approval for {device.name}")
        approved = True  
        if approved:
            device.install_update(new_version)
        else:
            print("Update not approved.")
class UpdateManager:
    def __init__(self, strategy):
        self.strategy = strategy

    def update_device(self, device, new_version):
        print("Checking version...")
        if device.current_version < new_version:
            self.strategy.apply_update(device, new_version)
        else:
            print(f"{device.name} is already up to date.")
device1 = Device("Laptop", 1.0)
device2 = Device("Phone", 1.5)
immediate = ImmediateUpdate()
scheduled = ScheduledUpdate()
manual = ManualApprovalUpdate()
manager = UpdateManager(immediate)
manager.update_device(device1, 2.0)
manager.strategy = scheduled
manager.update_device(device2, 2.0)
manager.strategy = manual
manager.update_device(device1, 3.0)
