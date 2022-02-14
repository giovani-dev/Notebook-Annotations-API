from unittest.mock import patch, Mock
import pytest

from src.api.notebook import view


class TestNotebookView:

    @pytest.mark.anyio
    @patch("src.api.notebook.view.Notebook.create")
    async def test_create__expected_valid_function_call(
        self,
        mock_notebook_create
    ):
        body = Mock()
        _create = await view.create(
            body=body
        )
        mock_notebook_create.assert_called_once_with(body)

    @pytest.mark.anyio
    @patch("src.api.notebook.view.Notebook.get")
    async def test_get__expected_valid_response_data(
            self,
            mock_notebook_get
    ):
        _get = await view.get(
            notebook_id="A502CE1EFF5696A67621D6368CFCA455FC3648F9"
        )

        mock_notebook_get.assert_called_once_with(
            "A502CE1EFF5696A67621D6368CFCA455FC3648F9"
        )

    @pytest.mark.anyio
    @patch("src.api.notebook.view.Notebook.put")
    async def test_put__expected_valid_function_call(
            self,
            mock_notebook_put
    ):
        body = Mock()
        _put = await view.put(
            notebook_id="A502CE1EFF5696A67621D6368CFCA455FC3648F9",
            body=body
        )

        mock_notebook_put.assert_called_once_with(
            body,
            "A502CE1EFF5696A67621D6368CFCA455FC3648F9"
        )

    @pytest.mark.anyio
    @patch("src.api.notebook.view.Notebook.patch")
    async def test_patch__expected_valid_function_call(
            self,
            mock_notebook_patch
    ):
        body = Mock()
        _patch = await view.patch(
            notebook_id="A502CE1EFF5696A67621D6368CFCA455FC3648F9",
            body=body
        )

        mock_notebook_patch.assert_called_once_with(
            body,
            "A502CE1EFF5696A67621D6368CFCA455FC3648F9"
        )

    @pytest.mark.anyio
    @patch("src.api.notebook.view.Notebook.list")
    async def test_list__expected_valid_function_call(
            self,
            mock_notebook_list
    ):
        mock_response = Mock()
        _list = await view.list(
            response=mock_response
        )

        mock_notebook_list.assert_called_once_with(mock_response)

    @pytest.mark.anyio
    @patch("src.api.notebook.view.Notebook.delete")
    async def test_list__expected_valid_function_call(
            self,
            mock_notebook_delete
    ):
        _list = await view.delete(
            notebook_id="A502CE1EFF5696A67621D6368CFCA455FC3648F9"
        )

        mock_notebook_delete.assert_called_once_with("A502CE1EFF5696A67621D6368CFCA455FC3648F9")
