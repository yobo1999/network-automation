def filter_devices_by_uptime(devices: list, threshold: int) -> list:
    # Input example:
    # devices = [
    #     {"hostname": "router1", "uptime": 120},
    #     {"hostname": "switch1", "uptime": 50},
    #     {"hostname": "router2", "uptime": 200},
    #     {"hostname": "switch2"}  # Missing uptime
    # ]
    # threshold = 100
    # Output: ["router1", "router2"]
    
    result = []
    if not devices:
        return
    for device in devices:
        uptime = device.get("uptime")
        if uptime is None:
                continue
        if isinstance(uptime, int):
            if uptime > threshold:
                result.append(device['hostname'])
        
        
            
    return sorted(result)

# Test cases
test_cases = [
    (
        [
            {"hostname": "router1", "uptime": 120},
            {"hostname": "switch1", "uptime": 50},
            {"hostname": "router2", "uptime": 200},
            {"hostname": "switch2"}
        ],
        100,
        ["router1", "router2"]
    ),
    ([], 50, []),  # Empty list
    (
        [
            {"hostname": "router1", "uptime": 20},
            {"hostname": "switch1"}  # Missing uptime
        ],
        50,
        []
    )  # No devices above threshold
]

# Run tests
for i, (devices, threshold, expected) in enumerate(test_cases, 1):
    result = filter_devices_by_uptime(devices, threshold)
    print(f"Test Case {i}:")
    print(f"Input: devices={devices}, threshold={threshold}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print(f"Result: {'Pass' if result == expected else 'Fail'}\n")

