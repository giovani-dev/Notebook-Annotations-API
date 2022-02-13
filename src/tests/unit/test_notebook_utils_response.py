from unittest.mock import patch, Mock

import pytest

from src.api.notebook.utils.response import notebook_response


class TestUtilsResponse:

    @pytest.mark.anyio
    @patch("src.api.notebook.utils.response.str")
    @patch("src.api.notebook.utils.response.NotebookResponse")
    async def test_notebook_response__expected_valid_function_call(
            self,
            mock_notebook_response,
            mock_str
    ):
        mock_document = Mock()
        mock_document.id = "1"
        mock_document.description = "test description"
        mock_document.creation_date = "test creation_date"
        mock_document.modification_date = "test modification_date"
        mock_document.annotations = "test annotations"

        mock_str.return_value = "1"

        await notebook_response(mock_document)

        mock_notebook_response.assert_called_once_with(
            id="1",
            description="test description",
            creation_date="test creation_date",
            modification_date="test modification_date",
            annotations="test annotations",
        )
        mock_str.assert_called_with("1")
        mock_document.assert_not_called()
