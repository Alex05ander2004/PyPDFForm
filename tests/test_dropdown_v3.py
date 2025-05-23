# -*- coding: utf-8 -*-

import os

from PyPDFForm import PdfWrapper


def test_schema(sample_template_with_dropdown):
    obj = PdfWrapper(sample_template_with_dropdown)

    for key, value in obj.schema["properties"].items():
        if key == "dropdown_1":
            assert value["maximum"] == 3

    assert obj.sample_data["dropdown_1"] == 3


def test_dropdown_not_specified(sample_template_with_dropdown):
    assert (
        PdfWrapper(sample_template_with_dropdown)
        .fill(
            {
                "test_1": "test_1",
                "test_2": "test_2",
                "test_3": "test_3",
                "check_1": True,
                "check_2": True,
                "check_3": True,
                "radio_1": 1,
            }
        )
        .read()
    )


def test_dropdown_one(sample_template_with_dropdown, pdf_samples, request):
    expected_path = os.path.join(pdf_samples, "dropdown", "test_dropdown_one.pdf")
    with open(expected_path, "rb+") as f:
        obj = PdfWrapper(sample_template_with_dropdown).fill(
            {
                "test_1": "test_1",
                "test_2": "test_2",
                "test_3": "test_3",
                "check_1": True,
                "check_2": True,
                "check_3": True,
                "radio_1": 1,
                "dropdown_1": 0,
            },
        )

        request.config.results["expected_path"] = expected_path
        request.config.results["stream"] = obj.read()

        expected = f.read()

        assert len(obj.read()) == len(expected)
        assert obj.read() == expected


def test_dropdown_one_flatten(sample_template_with_dropdown, pdf_samples, request):
    expected_path = os.path.join(pdf_samples, "dropdown", "test_dropdown_one_flatten.pdf")
    with open(expected_path, "rb+") as f:
        obj = PdfWrapper(sample_template_with_dropdown).fill(
            {
                "test_1": "test_1",
                "test_2": "test_2",
                "test_3": "test_3",
                "check_1": True,
                "check_2": True,
                "check_3": True,
                "radio_1": 1,
                "dropdown_1": 0,
            },
        )

        request.config.results["expected_path"] = expected_path
        request.config.results["stream"] = obj.read()

        expected = f.read()

        assert len(obj.read()) == len(expected)
        assert obj.read() == expected
