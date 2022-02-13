import pytest
from fastapi import HTTPException

from src.utils.http_exception import not_found


class TestUtilsHttpExpection:

    @pytest.mark.anyio
    async def test_not_found__expected_http_expection(self):
        with pytest.raises(HTTPException) as error:
            await not_found(
                data=None,
                error_message="error"
            )

        assert error.value.detail == 'error'
        assert error.value.status_code == 404
