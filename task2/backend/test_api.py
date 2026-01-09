"""
Simple test script to verify the API is working.
Run this after starting the Flask server.
"""

import requests
import json

API_BASE_URL = "http://localhost:5000"

def test_health_check():
    """Test the health check endpoint."""
    print("Testing health check endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/api/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_submit_review():
    """Test submitting a review."""
    print("\nTesting review submission...")
    test_data = {
        "user_rating": 4,
        "user_review": "Great service and friendly staff. The food was delicious!"
    }
    try:
        response = requests.post(
            f"{API_BASE_URL}/api/reviews",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status: {response.status_code}")
        if response.status_code == 201:
            print("Review submitted successfully!")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            return True
        else:
            print(f"Error: {response.json()}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_get_reviews():
    """Test getting all reviews."""
    print("\nTesting get all reviews...")
    try:
        response = requests.get(f"{API_BASE_URL}/api/admin/reviews")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data.get('reviews', []))} reviews")
            return True
        else:
            print(f"Error: {response.json()}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_get_stats():
    """Test getting statistics."""
    print("\nTesting get statistics...")
    try:
        response = requests.get(f"{API_BASE_URL}/api/admin/stats")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print(f"Stats: {json.dumps(response.json(), indent=2)}")
            return True
        else:
            print(f"Error: {response.json()}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("API Test Suite")
    print("=" * 50)
    print("\nMake sure the Flask server is running on http://localhost:5000")
    print("=" * 50)
    
    results = []
    results.append(("Health Check", test_health_check()))
    results.append(("Submit Review", test_submit_review()))
    results.append(("Get Reviews", test_get_reviews()))
    results.append(("Get Stats", test_get_stats()))
    
    print("\n" + "=" * 50)
    print("Test Results Summary")
    print("=" * 50)
    for test_name, passed in results:
        status = "PASSED" if passed else "FAILED"
        print(f"{test_name}: {status}")
