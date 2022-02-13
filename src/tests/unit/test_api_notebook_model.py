from unittest.mock import patch, Mock, call

import pytest

from src.api.notebook.model import Notebook


class TestNotebookModel:

    @pytest.mark.anyio
    @patch("src.api.notebook.model.Notebook.validate_annotations", name="mock_validate_annotations")
    @patch("src.api.notebook.model.BaseApiModel.create", name="mock_api_model_create")
    @patch("src.api.notebook.model.get_document_with_id", name="mock_get_document_with_id")
    @patch("src.api.notebook.model.notebook_response", name="mock_response")
    @patch("src.api.notebook.model.NotebookDocument", name="mock_document")
    async def test_create__expected_valid_function_calls(
            self,
            mock_document,
            mock_response,
            mock_get_document_with_id,
            mock_api_model_create,
            mock_validate_annotations
    ):
        mock_body = Mock(name="body")
        mock_body.annotations = ["annotation1", "annotation2"]

        base = Notebook()
        await base.create(
            body=mock_body
        )

        mock_validate_annotations.assert_called_once_with(["annotation1", "annotation2"])
        mock_api_model_create.assert_called_with(mock_body)
        mock_document.assert_not_called()
        mock_response.assert_not_called()
        mock_get_document_with_id.assert_not_called()
        mock_body.assert_not_called()

    @pytest.mark.anyio
    @patch("src.api.notebook.model.BaseApiModel.get", name="mock_api_model_get")
    @patch("src.api.notebook.model.get_document_with_id", name="mock_get_document_with_id")
    @patch("src.api.notebook.model.notebook_response", name="mock_response")
    @patch("src.api.notebook.model.NotebookDocument", name="mock_document")
    async def test_get__expected_valid_function_calls(
            self,
            mock_document,
            mock_response,
            mock_get_document_with_id,
            mock_api_model_get
    ):
        base = Notebook()
        await base.get(_id="1")

        mock_api_model_get.assert_called_with(
            _id="1",
            error_message="Notebook not found.",
        )
        mock_document.assert_not_called()
        mock_response.assert_not_called()
        mock_get_document_with_id.assert_not_called()

    @pytest.mark.anyio
    @patch("src.api.notebook.model.Notebook.validate_annotations", name="mock_validate_annotations")
    @patch("src.api.notebook.model.datetime", name="mock_datetime")
    @patch("src.api.notebook.model.BaseApiModel.put", name="mock_api_model_put")
    @patch("src.api.notebook.model.get_document_with_id", name="mock_get_document_with_id")
    @patch("src.api.notebook.model.notebook_response", name="mock_response")
    @patch("src.api.notebook.model.NotebookDocument", name="mock_document")
    async def test_put__expected_valid_function_calls(
            self,
            mock_document,
            mock_response,
            mock_get_document_with_id,
            mock_api_model_put,
            mock_datetime,
            mock_validate_annotations
    ):
        mock_datetime.now.return_value = "Teste 14H:30M"

        mock_document.description = "description"
        mock_document.modification_date = "modification_date"
        mock_document.annotations = "annotations"

        mock_body = Mock()
        mock_body.description = "teste description"
        mock_body.annotations = ["annotation1", "annotation2"]

        base = Notebook()
        await base.put(
            body=mock_body,
            _id="1"
        )

        mock_validate_annotations.assert_called_once_with(["annotation1", "annotation2"])
        mock_api_model_put.assert_called_with(
            body=mock_body,
            _id="1",
            error_message="Notebook not found.",
            set_parameters={
                "description": "teste description",
                "modification_date": "Teste 14H:30M",
                "annotations": ["annotation1", "annotation2"]
            }
        )
        mock_document.assert_not_called()
        mock_response.assert_not_called()
        mock_get_document_with_id.assert_not_called()
        mock_body.assert_not_called()
        mock_datetime.assert_not_called()

    @pytest.mark.anyio
    @patch("src.api.notebook.model.Notebook.validate_annotations", name="mock_validate_annotations")
    @patch("src.api.notebook.model.Notebook.patch_notebook", name="mock_patch_notebook")
    @patch("src.api.notebook.model.BaseApiModel.patch", name="mock_api_model_patch")
    @patch("src.api.notebook.model.get_document_with_id", name="mock_get_document_with_id")
    @patch("src.api.notebook.model.notebook_response", name="mock_response")
    @patch("src.api.notebook.model.NotebookDocument", name="mock_document")
    async def test_patch__expected_valid_function_calls(
            self,
            mock_document,
            mock_response,
            mock_get_document_with_id,
            mock_api_model_patch,
            mock_patch_notebook,
            mock_validate_annotations
    ):
        mock_body = Mock()
        mock_body.annotations = ["annotation1", "annotation2"]

        base = Notebook()
        await base.patch(
            body=mock_body,
            _id="1",
        )

        mock_validate_annotations.assert_called_once_with(["annotation1", "annotation2"])
        mock_api_model_patch.assert_called_with(
            body=mock_body,
            _id="1",
            error_message="Notebook not found.",
            patch_operation=mock_patch_notebook
        )
        mock_document.assert_not_called()
        mock_response.assert_not_called()
        mock_get_document_with_id.assert_not_called()
        mock_patch_notebook.assert_not_called()

    @pytest.mark.anyio
    @patch("src.api.notebook.model.BaseApiModel.list", name="mock_api_model_list")
    @patch("src.api.notebook.model.get_document_with_id", name="mock_get_document_with_id")
    @patch("src.api.notebook.model.notebook_response", name="mock_response")
    @patch("src.api.notebook.model.NotebookDocument", name="mock_document")
    async def test_list__expected_valid_function_calls(
            self,
            mock_document,
            mock_response,
            mock_get_document_with_id,
            mock_api_model_list
    ):
        mock_response_parameter = Mock()

        base = Notebook()
        await base.list(
            response=mock_response_parameter
        )

        mock_api_model_list.assert_called_once_with(mock_response_parameter)
        mock_get_document_with_id.assert_not_called()
        mock_response.assert_not_called()
        mock_document.assert_not_called()
        mock_response_parameter.assert_not_called()

    @pytest.mark.anyio
    @patch("src.api.notebook.model.BaseApiModel.delete", name="mock_api_model_delete")
    @patch("src.api.notebook.model.get_document_with_id", name="mock_get_document_with_id")
    @patch("src.api.notebook.model.notebook_response", name="mock_response")
    @patch("src.api.notebook.model.NotebookDocument", name="mock_document")
    async def test_delete__expected_valid_function_calls(
            self,
            mock_document,
            mock_response,
            mock_get_document_with_id,
            mock_api_model_delete
    ):
        base = Notebook()
        await base.delete(
            _id="1"
        )

        mock_api_model_delete.assert_called_once_with(
            _id="1",
            error_message="Notebook not found."
        )
        mock_get_document_with_id.assert_not_called()
        mock_response.assert_not_called()
        mock_document.assert_not_called()

    @pytest.mark.anyio
    async def test_patch_notebook__expected_values_change(self):
        mock_notebook = Mock()

        mock_body = Mock()
        mock_body.description = "teste description"
        mock_body.annotations = "teste annotations"

        await Notebook.patch_notebook(
            notebook=mock_notebook,
            body=mock_body
        )

        assert mock_notebook.description == "teste description"
        assert mock_notebook.annotations == "teste annotations"
        mock_notebook.assert_not_called()
        mock_body.assert_not_called()

    @pytest.mark.anyio
    @patch("src.api.notebook.model.AnnotationDocument", name="mock_annotation_document")
    @patch("src.api.notebook.model.get_document_with_id", name="mock_get_document_with_id")
    async def test_validate_annotations__valid_function_call(
            self,
            mock_get_document_with_id,
            mock_annotation_document
    ):
        annotations = ["1", "2"]

        await Notebook.validate_annotations(annotations)

        mock_get_document_with_id_calls = [
            call(
                _id="1",
                document_class=mock_annotation_document,
                error_message="Annotation 1 does not exist."
            ),
            call(
                _id="2",
                document_class=mock_annotation_document,
                error_message="Annotation 2 does not exist."
            )
        ]
        mock_get_document_with_id.assert_has_calls(mock_get_document_with_id_calls)
