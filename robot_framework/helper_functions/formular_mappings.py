"""
file to contain formular mappings

Ideally we wouldn't have to hardcode the mappings, but we the column names from the API are inconsistent in spelling and casing - therefore we need to map them to the correct column names in the Excel file.
"""

import ast

sundung_aarhus_mapping = {
    "serial": "Serial number",
    "created": "Oprettet",
    "completed": "Gennemført",
    "navn": "Navn",
    "cpr_nummer": "CPR-nummer",
    "ungdomsuddannelse_radio": "Ungdomsuddannelse",
    "henvendelsesaarsag": "Henvendelsesårsag",
    "hvordan_vil_du_kontaktes": "Hvordan vil du kontaktes?",
    "telefonnummer_": "Telefonnummer",
    "e_mailadresse": "Mail",
}

henvisningsskema_til_klinisk_hyp_mapping = {
    "serial": "Serial number",
    "created": "Oprettet",
    "completed": "Gennemført",
    "barnets_navn": "Barnets navn",
    "cpr_barnets_nummer": "Barnets CPR-nummer",
    "barnets_alder": "Barnets alder",
    "skole_privat": "Skole",
    "henvisers_navn": "Henvisers navn",
    "henvisers_stilling": "Henvisers stilling",
    "henvisers_e_mailadresse": "Henvisers e-mailadresse",
    "er_foraeldremyndigheds_indehavere_og_barnet_indstillet_paa_at_af": "Er der samtykke fra (begge) forældremyndighedsindehaver(e) til henvisning til klinisk hypnoterapi?",
    "er_barnet_indstillet_paa_at_afproeve_hypnoterapi_": "Er barnet indstillet på at afprøve hypnoterapi?",
    "hvad_er_barnets_primaere_udfordring_": "Hvad er barnets primære udfordring?",
    "hvor_laenge_har_udfordringen_varet_": "Hvor længe har udfordringen varet?",
    "hvilken_indflydelse_har_det_paa_barnets_trivsel_i_skoletid_": "Hvilken indflydelse har udfordringen på barnets trivsel i skoletid?",
    "hvilke_tiltag_er_ellers_ivaerksat_tidligere_afproevet_": "Hvilke tiltag er ellers iværksat/tidligere afprøvet?",
    "skolefravaer_den_seneste_maaned": "Skolefravær den seneste måned",
    "er_barnet_aktuelt_eller_tidligere_tilknyttet_en_af": "Er barnet, aktuelt eller tidligere, tilknyttet en af nedenstående?",
    "uddyb_gerne": "Uddyb gerne",
    "hvad_er_oensket_maal_for_forventning_til_effekt_af_hypnoterapi_": "Hvad er det ønskede konkrete mål for hypnoterapi"
}


def transform_form_submission(form_serial_number, form: dict, mapping: dict) -> dict:
    """
    Transforms a form submission dictionary using the provided mapping.

    For each field:
      - Replaces newline characters with a full stop and a space.
      - If the value is a string that looks like a list (e.g. "['Mail', 'SMS']"),
        converts it to a comma-separated string.

    Also adds additional fields from the form's "entity" section.

    Args:
        form_serial_number: The serial number from the form's entity.
        form (dict): The raw form submission data.
        mapping (dict): A dictionary mapping source keys to target Excel column names.

    Returns:
        dict: A new dictionary with keys matching the Excel sheet column names.
    """

    form_data = form.get("data", {})
    transformed = {}

    for source_key, target_column in mapping.items():
        value = form_data.get(source_key, None)

        # If value is a list, join the items with a comma and space.
        if isinstance(value, list):
            value = ", ".join(str(item) for item in value)

        # If value is a string, perform cleaning.
        elif isinstance(value, str):
            # Replace newline characters
            value = value.replace("\r\n", ". ").replace("\n", ". ")

            # If the string looks like a list, try to convert it.
            if value.startswith("[") and value.endswith("]"):
                try:
                    parsed = ast.literal_eval(value)

                    if isinstance(parsed, list):
                        value = ", ".join(str(item) for item in parsed)

                except Exception:
                    # Fallback: strip brackets and quotes if parsing fails
                    value = value.strip("[]").replace("'", "").replace('"', "").strip()

        transformed[target_column] = value

    # Retrieve additional fields from the "entity" portion
    try:
        created = form["entity"]["created"][0]["value"]

        completed = form["entity"]["completed"][0]["value"]

    except (KeyError, IndexError):
        created = None

        completed = None

    transformed["Serial number"] = form_serial_number

    transformed["Oprettet"] = created

    transformed["Gennemført"] = completed

    return transformed
