from unittest.mock import patch, call, AsyncMock

import pytest

from src.conf.connection import Connection


class TestConnection:

    @pytest.mark.anyio
    @patch("src.conf.connection.models")
    @patch("src.conf.connection.os.getenv")
    @patch("src.conf.connection.init_beanie")
    @patch("src.conf.connection.motor.motor_asyncio")
    async def test_mongo_db__expected_vaid_function_call(
            self,
            mock_motor_asyncio,
            mock_init_beanie,
            mock_os_getenv,
            mock_models
    ):
        mock_motor_asyncio_return = AsyncMock()
        mock_motor_asyncio_return.Annotate_db = "mongoDB"
        mock_motor_asyncio.AsyncIOMotorClient.return_value = mock_motor_asyncio_return
        mock_os_getenv.return_value = "TESTE"

        await Connection.mongo_db()

        mock_motor_asyncio.AsyncIOMotorClient.assert_called_with(
            "mongodb://TESTE:TESTE@TESTE/myFirstDatabase?ssl=true&replicaSet=atlas-k4659o-shard-0&authSource=admin&retryWrites=true&w=majority"
        )
        mock_os_getenv_calls = [
            call('MONGO_USER'),
            call('MONGO_PASSWORD'),
            call('MONGO_HOST')
        ]
        mock_os_getenv.assert_has_calls(mock_os_getenv_calls)
        mock_init_beanie.assert_called_with(
            database="mongoDB",
            document_models=mock_models
        )
