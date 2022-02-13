from unittest.mock import patch, Mock

import pytest

from src.api.annotation.model import Annotation


class TestAnnotationModel:

    @pytest.mark.anyio
    @patch("src.api.annotation.model.BaseApiModel.create", name="mock_api_model_create")
    @patch("src.api.annotation.model.get_document_with_id", name="mock_get_document_with_id")
    @patch("src.api.annotation.model.annotation_response", name="mock_response")
    @patch("src.api.annotation.model.AnnotationDocument", name="mock_document")
    async def test_create__expected_valid_function_calls(
            self,
            mock_document,
            mock_annotation_response,
            mock_get_document_with_id,
            mock_api_model_create
    ):
        mock_body = Mock(name="body")

        base = Annotation()
        await base.create(
            body=mock_body
        )

        mock_api_model_create.assert_called_with(mock_body)
        mock_document.assert_not_called()
        mock_annotation_response.assert_not_called()
        mock_get_document_with_id.assert_not_called()
        mock_body.assert_not_called()

    @pytest.mark.anyio
    @patch("src.api.annotation.model.BaseApiModel.get", name="mock_api_model_get")
    @patch("src.api.annotation.model.get_document_with_id", name="mock_get_document_with_id")
    @patch("src.api.annotation.model.annotation_response", name="mock_response")
    @patch("src.api.annotation.model.AnnotationDocument", name="mock_document")
    async def test_get__expected_valid_function_calls(
            self,
            mock_document,
            mock_annotation_response,
            mock_get_document_with_id,
            mock_api_model_get
    ):
        base = Annotation()
        await base.get(_id="1")

        mock_api_model_get.assert_called_with(
            _id="1",
            error_message="Annotation not found.",
        )
        mock_document.assert_not_called()
        mock_annotation_response.assert_not_called()
        mock_get_document_with_id.assert_not_called()

    @pytest.mark.anyio
    @patch("src.api.annotation.model.datetime", name="mock_datetime")
    @patch("src.api.annotation.model.BaseApiModel.put", name="mock_api_model_put")
    @patch("src.api.annotation.model.get_document_with_id", name="mock_get_document_with_id")
    @patch("src.api.annotation.model.annotation_response", name="mock_response")
    @patch("src.api.annotation.model.AnnotationDocument", name="mock_document")
    async def test_put__expected_valid_function_calls(
            self,
            mock_document,
            mock_annotation_response,
            mock_get_document_with_id,
            mock_api_model_put,
            mock_datetime
    ):
        mock_datetime.now.return_value = "Teste 14H:30M"

        mock_document.title = "title"
        mock_document.modification_date = "modification_date"
        mock_document.tags = "tags"

        mock_body = Mock()
        mock_body.title = "teste title"
        mock_body.tags = ["tag1", "tag2"]

        base = Annotation()
        await base.put(
            body=mock_body,
            _id="1"
        )

        mock_api_model_put.assert_called_with(
            body=mock_body,
            _id="1",
            error_message="Annotation not found.",
            set_parameters={
                "title": "teste title",
                "modification_date": "Teste 14H:30M",
                "tags": ["tag1", "tag2"]
            }
        )
        mock_document.assert_not_called()
        mock_annotation_response.assert_not_called()
        mock_get_document_with_id.assert_not_called()
        mock_body.assert_not_called()
        mock_datetime.assert_not_called()

    @pytest.mark.anyio
    @patch("src.api.annotation.model.Annotation.patch_annotation", name="mock_patch_annotation")
    @patch("src.api.annotation.model.BaseApiModel.patch", name="mock_api_model_patch")
    @patch("src.api.annotation.model.get_document_with_id", name="mock_get_document_with_id")
    @patch("src.api.annotation.model.annotation_response", name="mock_response")
    @patch("src.api.annotation.model.AnnotationDocument", name="mock_document")
    async def test_patch__expected_valid_function_calls(
            self,
            mock_document,
            mock_annotation_response,
            mock_get_document_with_id,
            mock_api_model_patch,
            mock_patch_annotation
    ):
        mock_body = Mock()

        base = Annotation()
        await base.patch(
            body=mock_body,
            _id="1",
        )

        mock_api_model_patch.assert_called_with(
            body=mock_body,
            _id="1",
            error_message="Annotation not found.",
            patch_operation=mock_patch_annotation
        )
        mock_document.assert_not_called()
        mock_annotation_response.assert_not_called()
        mock_get_document_with_id.assert_not_called()
        mock_patch_annotation.assert_not_called()

    @pytest.mark.anyio
    @patch("src.api.annotation.model.BaseApiModel.list", name="mock_api_model_list")
    @patch("src.api.annotation.model.get_document_with_id", name="mock_get_document_with_id")
    @patch("src.api.annotation.model.annotation_response", name="mock_response")
    @patch("src.api.annotation.model.AnnotationDocument", name="mock_document")
    async def test_list__expected_valid_function_calls(
            self,
            mock_document,
            mock_response,
            mock_get_document_with_id,
            mock_api_model_list
    ):
        mock_response_parameter = Mock()

        base = Annotation()
        await base.list(
            response=mock_response_parameter
        )

        mock_api_model_list.assert_called_once_with(mock_response_parameter)
        mock_get_document_with_id.assert_not_called()
        mock_response.assert_not_called()
        mock_document.assert_not_called()
        mock_response_parameter.assert_not_called()

    @pytest.mark.anyio
    @patch("src.api.annotation.model.BaseApiModel.delete", name="mock_api_model_delete")
    @patch("src.api.annotation.model.get_document_with_id", name="mock_get_document_with_id")
    @patch("src.api.annotation.model.annotation_response", name="mock_response")
    @patch("src.api.annotation.model.AnnotationDocument", name="mock_document")
    async def test_delete__expected_valid_function_calls(
            self,
            mock_document,
            mock_response,
            mock_get_document_with_id,
            mock_api_model_delete
    ):
        base = Annotation()
        await base.delete(
            _id="1"
        )

        mock_api_model_delete.assert_called_once_with(
            _id="1",
            error_message="Annotation not found."
        )
        mock_get_document_with_id.assert_not_called()
        mock_response.assert_not_called()
        mock_document.assert_not_called()

    @pytest.mark.anyio
    async def test_patch_annotation__expected_values_change(self):
        mock_annotation = Mock()

        mock_body = Mock()
        mock_body.title = "teste title"
        mock_body.tags = "teste tags"

        await Annotation.patch_annotation(
            annotation=mock_annotation,
            body=mock_body
        )

        assert mock_annotation.title == "teste title"
        assert mock_annotation.tags == "teste tags"
        mock_annotation.assert_not_called()
        mock_body.assert_not_called()
