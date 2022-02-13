from unittest.mock import patch, Mock

import pytest

from src.api.annotation.utils.response import annotation_response


class TestUtilsResponse:

    @pytest.mark.anyio
    @patch("src.api.annotation.utils.response.str")
    @patch("src.api.annotation.utils.response.AnnotationResponse")
    async def test_notebook_response__expected_valid_function_call(
            self,
            mock_annotation_response,
            mock_str
    ):
        mock_document = Mock()
        mock_document.id = "1"
        mock_document.title = "test title"
        mock_document.creation_date = "test creation_date"
        mock_document.modification_date = "test modification_date"
        mock_document.tags = "test tags"

        mock_str.return_value = "1"

        await annotation_response(mock_document)

        mock_annotation_response.assert_called_once_with(
            id="1",
            title="test title",
            creation_date="test creation_date",
            modification_date="test modification_date",
            tags="test tags",
        )
        mock_str.assert_called_with("1")
        mock_document.assert_not_called()
