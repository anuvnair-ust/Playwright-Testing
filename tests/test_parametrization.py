from playwright.sync_api import expect
import pytest
import time
import json
from pathlib import Path

URL ="https://www.playwrightautomation.com/practice.html"

@pytest.mark.parametrize(
    "name,email,address,status",
    [
        ("Anu", "anu@o.io", "asddjkn,\niuwqhid,\nuguhi",False),
        ("John Smith", "john.smith@example.com", "42 Main Street, Springfield",True),
        ("Zoë O'Brien-Lee", "zoe.obrien+test@example.co.uk", "Flat 3, 18 Rue de la Paix, Paris",False),
        ("A", "a@b.co", "1",False),
        ("Long Name " * 5, "long.email.address.for.testing@subdomain.example.org", "X" * 120,True)
    ],
    ids=["anu", "john-smith", "zoe-obrien-lee", "single-char", "long-values"])
def test_paramterization_hardcoded(page, name, email, address, status):
    page.goto(URL,
              wait_until="domcontentloaded"
              )
    name_field = page.get_by_test_id("input-name")
    email_field = page.get_by_placeholder("Enter your email")
    address_field = page.get_by_test_id("input-address")
    submit_button = page.get_by_role("button", name="Submit")
    submit_status = page.get_by_test_id("text-inputs-status")

    name_field.fill(name)
    email_field.fill(email)
    address_field.fill(address)
    expect(name_field).to_have_value(name)
    expect(email_field).to_have_value(email)
    expect(address_field).to_have_value(address)
    submit_button.click()
    if status:
        expect(submit_status).to_have_text("submitted")
    else:
        expect(submit_status).to_have_text("invalid")

ADDRESS_DATA = json.loads(
    (Path(__file__).resolve().parent.parent/"test_data"/"address_data.json").read_text(encoding="utf-8"))

@pytest.mark.parametrize(
    "data",ADDRESS_DATA,
    ids=["anu", "john-smith", "zoe-obrien-lee", "single-char", "long-values"])
def test_parametrization_json(page, data):
    page.goto(URL,
              wait_until="domcontentloaded"
              )
    name_field = page.get_by_test_id("input-name")
    email_field = page.get_by_placeholder("Enter your email")
    address_field = page.get_by_test_id("input-address")
    submit_button = page.get_by_role("button", name="Submit")
    submit_status = page.get_by_test_id("text-inputs-status")

    name_field.fill(data["name"])
    email_field.fill(data["email"])
    address_field.fill(data["address"])
    expect(name_field).to_have_value(data["name"])
    expect(email_field).to_have_value(data["email"])
    expect(address_field).to_have_value(data["address"])
    submit_button.click()
    if data["status"]:
        expect(submit_status).to_have_text("submitted")
    else:
        expect(submit_status).to_have_text("invalid")