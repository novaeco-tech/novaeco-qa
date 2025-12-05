# This Global Test links the local requirements together
@pytest.mark.requirement("REQ-RETAIL-FUNC-001")
@pytest.mark.requirement("REQ-MIND-FUNC-005")
def test_fiber_loop():
    # 1. Create return in Retail
    label = retail_api.create_return(...)
    # 2. Simulate sorting in Mind
    classification = mind_api.classify(image=shirt_img)
    # 3. Verify
    assert classification == "Cotton"