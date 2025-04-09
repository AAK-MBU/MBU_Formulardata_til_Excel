"""
file to contain formular mappings

Ideally we wouldn't have to hardcode the mappings, but we the column names from the API are inconsistent in spelling and casing - therefore we need to map them to the correct column names in the Excel file.
"""

import ast

from datetime import datetime

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
    "hvilke_tiltag_er_ellers_ivaerksat_tidligere_afproevet_": "Hvilke tiltag er ellers iværksat/tidligere afprøvet i skoletiden?",
    "er_barnet_aktuelt_eller_tidligere_tilknyttet_en_af": "Er barnet, aktuelt eller tidligere, tilknyttet en af nedenstående?",
    "uddyb_her_ppr": "Uddyb her - PPR",
    "uddyb_her_egen_laege": "Uddyb her - Egen læge",
    "uddyb_her_privatpraktiserende_psykolog": "Uddyb her - Privatpraktiserende psykolog",
    "uddyb_her_boerne_og_ungdompsykiatrien": "Uddyb her - Børne- og ungdompsykiatrien",
    "uddyb_her_sygehus": "Uddyb her - Sygehus",
    "uddyb_her_andet": "Uddyb her - Andet",
    "skolefravaer_den_seneste_maaned": "Skolefravær den seneste måned",
    "hvad_er_oensket_maal_for_forventning_til_effekt_af_hypnoterapi_": "Hvad er det ønskede konkrete mål for hypnoterapi"
}

spoergeskema_hypnoterapi_foer_fo_mapping = {
    "serial": "Serial number",
    "created": "Oprettet",
    "completed": "Gennemført",
    "navn": "Navn",
    "cpr_nummer": "CPR-nummer",
    "paa_vegne_af_mit_barn": "På vegne af mit barn",
    "barnets_navn": "Barnets navn",
    "cpr_nummer_barn": "Barnets CPR-nummer",
    "mit_barn_kommer_ikke_frem_i_listen": "Mit barn kommer ikke frem i listen",
    "barnets_navn_manuelt": "Barnets navn manuelt",
    "cpr_nummr_barnet_manuelt": "Barnets CPR-nummer manuelt",
    "er_voksen": "Er voksen",
    "fortael_mig_lidt_om_dit_liv": "Fortæl mig lidt om dit liv (din familie, din skole, fritidsinteresser, venner eller hvad du nu har lyst til)",
    "hvad_goer_dig_allermest_glad_": "Hvad gør dig mest glad?",
    "hvornaar_og_hvor_slapper_du_allerbedst_af_": "Hvornår og hvor slapper du allerbedst af?",
    "hvad_synes_du_selv_er_dine_staerke_gode_side_": "Hvad synes du selv er dine stærke/gode side?",
    "hvad_synes_andre_er_dine_staerke_gode_sider_": "Hvad synes andre er dine stærke/gode sider?",
    "fortael_om_det_problem_du_gerne_vil_have_hjaelp_til": "Fortæl om det problem, du gerne vil have hjælp til",
    "hvordan_paavirker_problemet_dit_liv": "Hvordan påvirker problemet dit liv",
    "hvad_har_du_taenkt_": "Har du tænkt over, hvorfor problemet er kommet? Hvornår begyndte det, hvad skete der i dit liv?",
    "hvilken_virkning_havde_behandlingen_": "Har du fået behandling fra andre? Hvis ja, af hvem og hvilken behandling? Og hvilken virkning havde det?",
    "hvad_kan_goere_problemet_vaerre_": "Hvad kan gøre problemet værre?",
    "hvad_kan_goere_problemet_bedre_": "Hvad kan gøre problemet bedre?",
    "beskriv_gerne_hvilke_problemer": "Er der andet, der fylder for dig?",
    'her_er_en_linke_med_prikker_fra_0_til_10_prik_0_betyder_det_vaer': 'Her er en linje med prikker fra 0 til 10. Prik 0 betyder "det værst mulige liv" for dig, og prik 10 betyder "det bedst mulige liv" for dig. Hvor på linjen synes du selv, du er for tiden?'
}


def transform_form_submission(form_serial_number, form: dict, mapping: dict) -> dict:
    """
    Transforms a form submission dictionary using the provided mapping.

    For each field:
      - Replaces newline characters with a full stop and a space.
      - If the value is a string that looks like a list (e.g. "['Mail', 'SMS']"),
        converts it to a comma-separated string.

    Also adds additional fields from the form's "entity" section, formatting date/time fields.

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

    # Retrieve additional fields from the "entity" portion and format the dates
    try:
        created_str = form["entity"]["created"][0]["value"]

        completed_str = form["entity"]["completed"][0]["value"]

        # Convert ISO date strings to datetime objects and reformat them
        created_dt = datetime.fromisoformat(created_str)

        completed_dt = datetime.fromisoformat(completed_str)

        # Format as "YYYY-MM-DD HH:MM:SS"
        created = created_dt.strftime("%Y-%m-%d %H:%M:%S")

        completed = completed_dt.strftime("%Y-%m-%d %H:%M:%S")

    except (KeyError, IndexError, ValueError):
        created = None

        completed = None

    transformed["Serial number"] = form_serial_number

    transformed["Oprettet"] = created

    transformed["Gennemført"] = completed

    return transformed
