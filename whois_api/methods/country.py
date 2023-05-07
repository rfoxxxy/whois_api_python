from whois_api.methods.base import MethodBase
from whois_api.types import Country
from whois_api.types.exceptions import OptionalParameterError


class CountryMethod(MethodBase):
    async def info_exists(
        self,
        country_alpha: str | int | None = None,
        country_fips: str | None = None,
        country_location_id: int | None = None,
    ) -> bool:
        """The method allows you to check the existence of information about a country by one of three parameters: country_alpha, country_fips or country_location_id.

        Args:
            country_alpha (str | int, optional): Two-letter, three-letter or numeric country code
                according to ISO 3166 standard, for example, RU for Russia or US for the United States of America.
                Not case sensitive. If this parameter is specified, other country parameters are ignored. Defaults to None.
            country_fips (str, optional): The country code according to the FIPS 10-4 standard
                (for example, US for the United States or RS for Russia).
                If this parameter is specified and country_alpha is not specified,
                then this parameter is used to determine the country. Defaults to None.
            country_location_id (int, optional): The country ID in the GeoNames database
                (for example, 6252001 for the United States or 2017370 for Russia).
                If this parameter is specified and country_alpha and country_fips are not specified,
                then this parameter is used to determine the country. Defaults to None.

        Raises:
            OptionalParameterError: None of optional parameters are used

        Returns:
            bool: Country existence
        """
        if not country_alpha and not country_fips and not country_location_id:
            raise OptionalParameterError(
                "one of optional parameters must be used"
            )
        return (
            await self.api_request(
                "info_exists",
                {
                    "country_alpha": country_alpha,
                    "country_fips": country_fips,
                    "country_location_id": country_location_id,
                },
            )
        ).output[0]

    async def info(
        self,
        country_alpha: str | int | None = None,
        country_fips: str | None = None,
        country_location_id: int | None = None,
    ) -> Country:
        """The method allows you to get information about a country by one of three parameters: country_alpha, country_fips or country_location_id.

        Args:
            country_alpha (str | int, optional): Two-letter, three-letter or numeric country code
                according to ISO 3166 standard, for example, RU for Russia or US for the United States of America.
                Not case sensitive. If this parameter is specified, other country parameters are ignored. Defaults to None.
            country_fips (str, optional): The country code according to the FIPS 10-4 standard
                (for example, US for the United States or RS for Russia).
                If this parameter is specified and country_alpha is not specified,
                then this parameter is used to determine the country. Defaults to None.
            country_location_id (int, optional): The country ID in the GeoNames database
                (for example, 6252001 for the United States or 2017370 for Russia).
                If this parameter is specified and country_alpha and country_fips are not specified,
                then this parameter is used to determine the country. Defaults to None.

        Raises:
            OptionalParameterError: None of optional parameters are used

        Returns:
            Country: Country Information object
        """
        if not country_alpha and not country_fips and not country_location_id:
            raise OptionalParameterError(
                "one of optional parameters must be used"
            )
        return (
            await self.api_request(
                "info",
                {
                    "country_alpha": country_alpha,
                    "country_fips": country_fips,
                    "country_location_id": country_location_id,
                },
            )
        ).output[0]

    async def is_neighbour(  # pylint: disable=too-many-arguments
        self,
        neighbour_1_country_alpha: str | int | None = None,
        neighbour_1_country_fips: str | None = None,
        neighbour_1_country_location_id: int | None = None,
        neighbour_2_country_alpha: str | int | None = None,
        neighbour_2_country_fips: str | None = None,
        neighbour_2_country_location_id: int | None = None,
    ) -> bool:
        """The method allows you to check whether two countries are neighbors by one of three parameters: neighbor_(n)_country_alpha, neighbor_(n)_country_fips or neighbor_(n)_country_location_id.

        Args:
            neighbour_1_country_alpha (str | int, optional): Two-letter, three-letter or numeric country code of 1st country
                according to ISO 3166 standard, for example, RU for Russia or US for the United States of America.
                Not case sensitive. If this parameter is specified, other country parameters are ignored. Defaults to None.
            neighbour_1_country_fips (str, optional): The country code of 1st country according to the FIPS 10-4 standard
                (for example, US for the United States or RS for Russia).
                If this parameter is specified and country_alpha is not specified,
                then this parameter is used to determine the country. Defaults to None.
            neighbour_1_country_location_id (int, optional): The country ID of 1st country in the GeoNames database
                (for example, 6252001 for the United States or 2017370 for Russia).
                If this parameter is specified and country_alpha and country_fips are not specified,
                then this parameter is used to determine the country. Defaults to None.
            neighbour_2_country_alpha (str | int, optional): Two-letter, three-letter or numeric country code of 2nd country
                according to ISO 3166 standard, for example, RU for Russia or US for the United States of America.
                Not case sensitive. If this parameter is specified, other country parameters are ignored. Defaults to None.
            neighbour_2_country_fips (str, optional): The country code of 2nd country according to the FIPS 10-4 standard
                (for example, US for the United States or RS for Russia).
                If this parameter is specified and country_alpha is not specified,
                then this parameter is used to determine the country. Defaults to None.
            neighbour_2_country_location_id (int, optional): The country ID of 2nd country in the GeoNames database
                (for example, 6252001 for the United States or 2017370 for Russia).
                If this parameter is specified and country_alpha and country_fips are not specified,
                then this parameter is used to determine the country. Defaults to None.

        Raises:
            OptionalParameterError: None of optional parameters for 1st country are used
            OptionalParameterError: None of optional parameters for 2nd country are used

        Returns:
            bool
        """
        if (
            not neighbour_1_country_alpha
            and not neighbour_1_country_fips
            and not neighbour_1_country_location_id
        ):
            raise OptionalParameterError(
                "one of optional parameters must be used for neighbour_1"
            )
        if (
            not neighbour_2_country_alpha
            and not neighbour_2_country_fips
            and not neighbour_2_country_location_id
        ):
            raise OptionalParameterError(
                "one of optional parameters must be used for neighbour_2"
            )
        return (
            await self.api_request(
                "is_neighbour",
                {
                    "neighbour_1_country_alpha": neighbour_1_country_alpha,
                    "neighbour_1_country_fips": neighbour_1_country_fips,
                    "neighbour_1_country_location_id": neighbour_1_country_location_id,
                    "neighbour_2_country_alpha": neighbour_2_country_alpha,
                    "neighbour_2_country_fips": neighbour_2_country_fips,
                    "neighbour_2_country_location_id": neighbour_2_country_location_id,
                },
            )
        ).output[0]
