from unittest.mock import patch, Mock, AsyncMock
from uuid import UUID

import pytest

from src.utils.query import get_document_with_id


class TestUtilsQuery:

    @pytest.mark.anyio
    @patch("src.utils.query.str", name="mock_str")
    @patch("src.utils.query.isinstance", return_value=True, name="mock_isinstance")
    @patch("src.utils.query.not_found", return_value="1", name="mock_not_found")
    @patch("src.utils.query.UUID", name="mock_uuid")
    async def test_get_document_with_id__expeted_string_to_UUID_tranform(
            self,
            mock_uuid,
            mock_not_found,
            mock_isinstance,
            mock_str
    ):
        mock_uuid.return_value = "1"

        mock_document = AsyncMock(name="mock_document")
        mock_document.id = "1"
        mock_document.find_one.return_value = "documento - teste"

        await get_document_with_id(
            _id="1",
            document_class=mock_document,
            error_message="erro teste"
        )

        mock_isinstance.assert_called_once_with("1", mock_str)
        mock_uuid.assert_called_once_with("1")
        mock_document.find_one.assert_called_once_with(True)
        mock_not_found.assert_called_once_with(
            data="documento - teste",
            error_message="erro teste"
        )
