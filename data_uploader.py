import asyncio
import httpx
import threading
humans_detected = 0

def update_humans_detected(detected): 
    global humans_detected
    humans_detected = detected

async def send_post_request(url, token, payload):
    headers = {
        'Authorization': f'Basic {token}',
        'Content-Type': 'application/json',
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        return response

async def send_data():
    url = 'https://transport.desolve.io/api/v1/dataflow/submit'  # Replace with your actual URL
    token = 'aG9yczo1b3BHNkx5VlBYTzJURGdiNkVNY0tyL1UxLzRyY3FCUlcwanlNTjF0a3ZTVng2YUM1NTg3T2tucDdVN0FUUXk5'

    while True:
        payload = {
            "humansDetected": humans_detected,
        }  # Replace with your actual JSON payload

        print(payload)
        response = await send_post_request(url, token, payload)
        
        print(f"Status Code: {response.status_code}")
        print("Response Content:")
        print(response.text)

        await asyncio.sleep(5)

def start_send_data_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(send_data())
    finally:
        loop.close()
