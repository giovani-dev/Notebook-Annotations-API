from unittest.mock import patch, Mock
import pytest

from src.api.annotation import view


class TestAnnotationView:

    @pytest.mark.anyio
    @patch("src.api.annotation.view.Annotation.create")
    async def test_create__expected_valid_input_data_and_reponse_data(
        self,
        mock_annotation_create
    ):
        body = Mock()
        _create = await view.create(
            body=body
        )
        mock_annotation_create.assert_called_once_with(body)

    @pytest.mark.anyio
    @patch("src.api.annotation.view.Annotation.get")
    async def test_get__expected_valid_response_data(
            self,
            mock_annotation_get
    ):
        _get = await view.get(
            annotation_id="A502CE1EFF5696A67621D6368CFCA455FC3648F9"
        )

        mock_annotation_get.assert_called_once_with(
            "A502CE1EFF5696A67621D6368CFCA455FC3648F9"
        )

    @pytest.mark.anyio
    @patch("src.api.annotation.view.Annotation.put")
    async def test_put__expected_valid_input_data_and_reponse_data(
            self,
            mock_annotation_put
    ):
        body = Mock()
        _put = await view.put(
            annotation_id="A502CE1EFF5696A67621D6368CFCA455FC3648F9",
            body=body
        )

        mock_annotation_put.assert_called_once_with(
            body,
            "A502CE1EFF5696A67621D6368CFCA455FC3648F9"
        )

    @pytest.mark.anyio
    @patch("src.api.annotation.view.Annotation.patch")
    async def test_patch__expected_valid_input_data_and_reponse_data(
            self,
            mock_annotation_patch
    ):
        body = Mock()
        _patch = await view.patch(
            annotation_id="A502CE1EFF5696A67621D6368CFCA455FC3648F9",
            body=body
        )

        mock_annotation_patch.assert_called_once_with(
            body,
            "A502CE1EFF5696A67621D6368CFCA455FC3648F9"
        )

    @pytest.mark.anyio
    @patch("src.api.annotation.view.Annotation.list")
    async def test_list__expected_valid_reponse_data(
            self,
            mock_annotation_list
    ):
        mock_response = Mock()
        _list = await view.list(
            response=mock_response
        )

        mock_annotation_list.assert_called_once_with(mock_response)

    @pytest.mark.anyio
    @patch("src.api.annotation.view.Annotation.delete")
    async def test_list__expected_valid_function_call(
            self,
            mock_annotation_delete
    ):
        _list = await view.delete(
            annotation_id="A502CE1EFF5696A67621D6368CFCA455FC3648F9"
        )

        mock_annotation_delete.assert_called_once_with("A502CE1EFF5696A67621D6368CFCA455FC3648F9")

