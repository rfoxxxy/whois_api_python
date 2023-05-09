# pylint: disable=R0801
from typing import List

from whois_api.methods.base import MethodBase
from whois_api.types import Language


class LanguageMethod(MethodBase):
    category_name = "language"

    async def info_exists(self, language_alpha: str) -> bool:
        """The method allows you to check the existence of information about the language by the language_alpha parameter.

        Args:
            language_alpha (str): A two-letter or three-letter language code according to the ISO 639 standard,
                which is used for the classification and identification of languages.
                For example, en is the code for English, ru is for Russian, fra is for French. Not case sensitive.

        Returns:
            bool: Information existence
        """
        return (
            await self.api_request(
                "info_exists", {"language_alpha": language_alpha}
            )
        ).output[0]

    async def info(self, language_alpha: str) -> Language:
        """The method allows you to get information about the language by the language_alpha parameter.

        Args:
            language_alpha (str): A two-letter or three-letter language code according to the ISO 639 standard,
                which is used for the classification and identification of languages.
                For example, en is the code for English, ru is for Russian, fra is for French. Not case sensitive.

        Returns:
            Language: Language Information object
        """
        return (
            await self.api_request("info", {"language_alpha": language_alpha})
        ).output[0]

    async def list_by_country(
        self,
        country_alpha: str | int | None = None,
        country_fips: str | None = None,
        country_location_id: int | None = None,
    ) -> List[Language]:
        """The method allows you to get a list of languages used in a particular country
           by one of three parameters: country_alpha, country_fips or country_location_id.

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

        Returns:
            List[Language]: List of Language objects
        """
        return (
            await self.api_request(
                "list_by_country",
                {
                    "country_alpha": country_alpha,
                    "country_fips": country_fips,
                    "country_location_id": country_location_id,
                },
            )
        ).output

    async def exists_by_country(
        self,
        language_alpha: str,
        country_alpha: str | int | None = None,
        country_fips: str | None = None,
        country_location_id: int | None = None,
    ) -> bool:
        """The method allows you to check whether a certain language is used in a certain country
           by the parameters language_alpha and country_alpha, country_fips or country_location_id.

        Args:
            language_alpha (str): A two-letter or three-letter language code according to the ISO 639 standard,
                which is used for the classification and identification of languages.
                For example, en is the code for English, ru is for Russian, fra is for French. Not case sensitive.
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

        Returns:
            bool
        """
        return (
            await self.api_request(
                "exists_by_country",
                {
                    "language_alpha": language_alpha,
                    "country_alpha": country_alpha,
                    "country_fips": country_fips,
                    "country_location_id": country_location_id,
                },
            )
        ).output[0]
