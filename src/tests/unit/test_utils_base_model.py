from unittest.mock import Mock, AsyncMock, patch, call

import pytest

from src.utils.base.model import BaseApiModel


class TestBaseApiModel:

    @pytest.mark.anyio
    @patch("src.utils.base.model.datetime")
    async def test_create__expected_valid_function_calls(
            self,
            mock_datetime
    ):
        mock_datetime.now.return_value = "Teste 14H:30M"

        mock_document = Mock()
        mock_document_to_async = AsyncMock()
        mock_document_to_async.insert.return_value = "cadastrado"
        mock_document.return_value = mock_document_to_async

        mock_response = AsyncMock()

        mock_get_document_with_id = AsyncMock()

        body = Mock()
        body.dict.return_value = {
            "title": "teste 123",
            "tags": ["tag1", "tag2"]
        }

        base = BaseApiModel(
            document=mock_document,
            response=mock_response,
            get_document_with_id=mock_get_document_with_id,
        )
        await base.create(body=body)

        mock_document.assert_called_once_with(
            creation_date="Teste 14H:30M",
            modification_date="Teste 14H:30M",
            title="teste 123",
            tags=["tag1", "tag2"]
        )
        mock_response.assert_called_once_with(document="cadastrado")
        mock_document_to_async.insert.assert_called_once()
        mock_get_document_with_id.assert_not_called()

    @pytest.mark.anyio
    async def test_get__expected_valid_function_calls(self):
        mock_document = Mock()

        mock_response = AsyncMock()

        mock_get_document_with_id = AsyncMock()
        mock_get_document_with_id.return_value = "teste - document"

        base = BaseApiModel(
            document=mock_document,
            response=mock_response,
            get_document_with_id=mock_get_document_with_id,
        )

        await base.get(
            _id="1",
            error_message="erro de teste unitario"
        )

        mock_get_document_with_id.assert_called_once_with(
            _id="1",
            document_class=mock_document,
            error_message="erro de teste unitario",
        )
        mock_response.assert_called_once_with(
            document="teste - document"
        )
        mock_document.assert_not_called()

    @pytest.mark.anyio
    async def test_put__expected_valid_function_calls(self):
        mock_document = Mock()

        mock_response = AsyncMock()

        mock_get_document_with_id = AsyncMock()
        mock_get_document_with_id_return = AsyncMock()
        mock_get_document_with_id.return_value = mock_get_document_with_id_return

        body = Mock()
        body.dict.return_value = {
            "title": "teste 123",
            "tags": ["tag1", "tag2"]
        }

        set_parameters = {"document_field": "document_value"}

        base = BaseApiModel(
            document=mock_document,
            response=mock_response,
            get_document_with_id=mock_get_document_with_id,
        )
        await base.put(
            body=body,
            _id="1",
            error_message="erro de teste unitario",
            set_parameters=set_parameters
        )

        mock_get_document_with_id.assert_called_once_with(
            _id="1",
            document_class=mock_document,
            error_message="erro de teste unitario",
        )
        mock_get_document_with_id_return.set.assert_called_once()
        mock_response.assert_called_once_with(
            document=mock_get_document_with_id_return
        )
        mock_document.assert_not_called()

    @pytest.mark.anyio
    @patch("src.utils.base.model.datetime")
    async def test_patch__expected_valid_function_calls(
            self,
            mock_datetime,
    ):
        mock_datetime.now.return_value = "Teste 14H:30M"

        mock_document = Mock(name="mock_document")

        mock_response = AsyncMock(name="mock_response")

        mock_get_document_with_id = AsyncMock(name="mock_get_document_with_id")
        mock_get_document_with_id_return = AsyncMock(name="mock_get_document_with_id_return")
        mock_get_document_with_id.return_value = mock_get_document_with_id_return

        mock_patch_operation = AsyncMock(name="mock_patch_operation")

        body = Mock()

        base = BaseApiModel(
            document=mock_document,
            response=mock_response,
            get_document_with_id=mock_get_document_with_id,
        )
        await base.patch(
            body=body,
            _id="1",
            error_message="erro de teste unitario",
            patch_operation=mock_patch_operation
        )

        mock_get_document_with_id.assert_called_once_with(
            _id="1",
            document_class=mock_document,
            error_message="erro de teste unitario",
        )
        mock_patch_operation.assert_called_once_with(
            mock_get_document_with_id_return, body
        )
        assert mock_get_document_with_id_return.modification_date == "Teste 14H:30M"
        mock_get_document_with_id_return.save.assert_called_once()
        mock_response.assert_called_once_with(
            document=mock_get_document_with_id_return
        )
        mock_document.assert_not_called()

    @pytest.mark.anyio
    @patch("src.utils.base.model.paginate")
    async def test_list__expected_valid_function_calls(
            self,
            mock_pagination
    ):
        mock_document = Mock(name="mock_document")
        mock_find_all_return = AsyncMock(name="mock_find_all")
        mock_find_all_return.to_list.return_value = ["dado1", "dado2"]
        mock_document.find_all.return_value = mock_find_all_return

        mock_get_document_with_id = AsyncMock(name="mock_get_document_with_id")

        mock_response = AsyncMock(name="mock_response")
        mock_response.return_value = "response teste"

        mock_response_parameter = Mock(name="mock_response_parameter")

        base = BaseApiModel(
            document=mock_document,
            response=mock_response,
            get_document_with_id=mock_get_document_with_id,
        )
        await base.list(response=mock_response_parameter)

        mock_document.assert_not_called()
        mock_document.find_all.assert_called_once()
        mock_find_all_return.to_list.assert_called_once()
        mock_response_calls = [
            call(document="dado1"),
            call(document="dado2")
        ]
        mock_response.assert_has_calls(mock_response_calls)
        mock_pagination.assert_called_once_with(
            ["response teste", "response teste"]
        )
        mock_get_document_with_id.assert_not_called()
        mock_document.assert_not_called()

    @pytest.mark.anyio
    @patch("src.utils.base.model.Response")
    async def test_delete__expected_valid_function_calls(
            self,
            mock_fastapi_response
    ):
        mock_document = Mock(name="mock_document")

        mock_get_document_with_id_return = AsyncMock(name="mock_get_document_with_id_return")
        mock_get_document_with_id = AsyncMock(name="mock_get_document_with_id")
        mock_get_document_with_id.return_value = mock_get_document_with_id_return

        mock_response = AsyncMock(name="mock_response")

        base = BaseApiModel(
            document=mock_document,
            response=mock_response,
            get_document_with_id=mock_get_document_with_id,
        )
        await base.delete(
            _id="1",
            error_message="teste menssagem de erro"
        )

        mock_get_document_with_id.assert_called_once_with(
            _id="1",
            document_class=mock_document,
            error_message="teste menssagem de erro",
        )
        mock_get_document_with_id_return.delete.assert_called_once()
        mock_fastapi_response.assert_called_with(
            status_code=204
        )
        mock_document.assert_not_called()
        mock_response.assert_not_called()
