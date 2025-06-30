"""
file to contain formular mappings

Ideally we wouldn't have to hardcode the mappings, but we the column names from the API are inconsistent in spelling and casing - therefore we need to map them to the correct column names in the Excel file.
"""

import ast

from datetime import datetime

basisteam_spoergeskema_til_fagpe_mapping = {
    "serial": "Serial number",
    "created": "Oprettet",
    "completed": "Gennemført",
    "fagpersonalets_navn": "Fagpersonalets navn",
    "fagpersonalets_stilling": "Fagpersonalets stilling",
    "skole_privat": "Skole/institution",
    "barnets_navn": "Barnets navn",
    "spoergsmaal_fagperson_tabel": {
        "spg_fagperson_1": 'Forløbet hjalp barnet',
        "spg_fagperson_2": 'Forløbet hjalp os på skolen/institutionen',
        "spg_fagperson_3": 'Hvis et andet barn havde brug for denne form for hjælp, ville jeg anbefale Basisteam',
        "spg_fagperson_4": 'Jeg følte mig passende informeret om meningen, formålet og forløbet',
        "spg_fagperson_5": 'Under forløbet blev vi på skolen/institutionen rustet til at håndtere elevens problemer på en positiv måde',
        "spg_fagperson_6": 'Under forløbet opnåede jeg en bedre forståelse af barnets psykiske tilstand',
        "spg_fagperson_7": 'Jeg havde tillid til Basisteam',
        "spg_fagperson_9": 'Sparringsmøderne med Basisteam var brugbare',
    },
    "hvad_var_rigtig_godt_ved_forloebet": "Hvad var rigtig godt ved Basisteam?",
    "var_der_noget_du_ikke_syntes_om_eller_noget_der_kan_forbedres": "Var der noget, du ikke synes om eller noget, der kan forbedres?",
    "er_der_andet_du_oensker_at_fortaelle_os_om_det_forloeb_du_har_haft": "Er der andet, du ønsker at fortælle os om det forløb, I som skole/institution har deltaget i?",
}

basisteam_spoergeskema_til_forae_mapping = {
    "serial": "Serial number",
    "created": "Oprettet",
    "completed": "Gennemført",
    "navn": "Navn",
    "cpr_nummer": "CPR-nummer",
    "paa_vegne_af_mit_barn": "På vegne af mit barn",
    "mit_barn_kommer_ikke_frem_i_listen": "Mit barn kommer ikke frem i listen",
    "barnets_navn": "Barnets navn",
    "cpr_nummer_barn": "Barnets CPR-nummer",
    "barnets_navn_manuelt": "Barnets navn manuelt",
    "cpr_nummr_barnet_manuelt": "Barnets CPR-nummer manuelt",
    "spoergsmaal_foraelder_tabel": {
        "spg_foraelder_1": 'Forløbet hjalp mit barn',
        "spg_foraelder_2": 'Forløbet hjalp mig',
        "spg_foraelder_3": 'Hvis en ven havde brug for denne form for hjælp, ville jeg anbefale vedkommende forløbet',
        "spg_foraelder_4": 'Jeg følte mig passende informeret om meningen, formålet og forløbet',
        "spg_foraelder_5": 'Vi har det bedre i familien nu, end før forløbet begyndte',
        "spg_foraelder_6": 'Under forløbet blev jeg i stand til at forandre min adfærd over for mit barn på en positiv måde',
        "spg_foraelder_7": 'Under forløbet opnåede jeg en bedre forståelse af mit barns psykiske tilstand',
        "spg_foraelder_8": 'Jeg havde tillid til Basisteam',
    },
    "hvad_var_rigtig_godt_ved_forloebet": "Hvad var rigtig godt ved forløbet?",
    "var_der_noget_du_ikke_syntes_om_eller_noget_der_kan_forbedres": "Var der noget, du ikke synes om eller noget, der kan forbedres?",
    "er_der_andet_du_oensker_at_fortaelle_os_om_det_forloeb_du_har_haft": "Er der andet, du ønsker at fortælle os om det forløb, du har haft?",
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

opfoelgende_spoergeskema_hypnote_mapping = {
    "serial": "Serial number",
    "created": "Oprettet",
    "completed": "Gennemført",
    "navn": "Navn",
    "cpr_nummer": "CPR-nummer",
    "paa_vegne_af_mit_barn": "På vegne af mit barn",
    "mit_barn_kommer_ikke_frem_i_listen": "Mit barn kommer ikke frem i listen",
    "barnets_navn": "Barnets navn",
    "cpr_nummer_barn": "Barnets CPR-nummer",
    "barnets_navn_manuelt": "Barnets navn manuelt",
    "cpr_nummr_barnet_manuelt": "Barnets CPR-nummer manuelt",
    "er_voksen": "Er voksen",
    "spoergsmaal_barn_tabel": {
        "spg_barn_1": "Behandlingen hjalp mig (barn)",
        "spg_barn_2": "Vi har det bedre i familien nu, end før behandlingen begyndte (barn)",
        "spg_barn_3": "Hvis en ven havde brug for denne form for hjælp, ville jeg anbefale ham/hende behandlingen (barn)",
        "spg_barn_4": "Behandlerne forstod det vigtigste af mine bekymringer og problemer",
        "spg_barn_5": "Jeg havde tillid til behandleren",
        "spg_barn_6": "Behandlingen medførte, at jeg fik det dårligere (barn)",
        "spg_barn_7": "Efter behandlingen har jeg fået mere lyst til at være sammen med mine venner",
    },
    "her_er_plads_til_at_du_kan_skrive_hvad_du_taenker_eller_foeler_o": "Her er plads til, at du kan skrive, hvad du tænker eller føler om behandlingen",
    "spoergsmaal_foraelder_tabel": {
        "spg_foraelder_1": "Behandlingen hjalp mit barn",
        "spg_foraelder_2": "Behandlingen hjalp mig (forælder)",
        "spg_foraelder_3": "Hvis en ven havde brug for denne form for hjælp, ville jeg anbefale vedkommende behandlingen (forælder)",
        "spg_foraelder_4": "Jeg følte mig passende informeret om meningen, formålet og forløbet af behandlingen",
        "spg_foraelder_5": "Vi har det bedre i familien nu, end før behandlingen begyndte (forælder)",
        "spg_foraelder_6": "Under behandlingen blev jeg i stand til at forandre min adfærd over for mit barn på en positiv måde",
        "spg_foraelder_7": "Under behandlingen opnåede jeg en bedre forståelse af mit barns psykiske tilstand",
        "spg_foraelder_8": "Jeg havde tillid til vores behandler",
        "spg_foraelder_9": "Behandlingen medførte, at mit barn fik det dårligere",
        "spg_foraelder_10": "Behandlingen medførte, at jeg fik det dårligere (forælder)",
    },
    "her_kan_du_selv_skrive_dine_kommentarer": "Her kan du selv skrive dine kommentarer",
    "hvad_var_rigtig_godt_ved_forloebet": "Hvad var rigtig godt ved forløbet?",
    "var_der_noget_du_ikke_syntes_om_eller_noget_der_kan_forbedres": "Var der noget du ikke synes om eller noget der kan forbedres?",
    "er_der_andet_du_oensker_at_fortaelle_os_om_det_forloeb_du_har_haft": "Er der andet du ønsker at fortælle os, om det forløb du har haft?",
}

foraelder_en_god_overgang_fra_hj_mapping = {
    "serial": "Serial number",
    "created": "Oprettet",
    "completed": "Gennemført",
    "navn": "Navn",
    "cpr_nummer": "CPR-nummer",
    "paa_vegne_af_mit_barn": "På vegne af mit barn",
    "mit_barn_kommer_ikke_frem_i_listen": "Mit barn kommer ikke frem i listen",
    "barnets_navn": "Barnets navn",
    "cpr_nummer_barn": "Barnets CPR-nummer",
    "barnets_navn_manuelt": "Barnets navn manuelt",
    "cpr_nummr_barnet_manuelt": "Barnets CPR-nummer manuelt",
    "spoergsmaal_foraelder_tabel": {
        "spg_foraelder_1": "Indsatsen hjalp mit barns opstart i vuggestue/dagpleje",
        "spg_foraelder_2": "Indsatsen gav mig tryghed i mit barns opstart i vuggestue/dagpleje",
        "spg_foraelder_3": "Overgangsmødet med sundhedsplejerske og pædagog var meningsfuldt",
        "spg_foraelder_4": "Jeg oplevede, at samarbejdet mellem sundhedsplejerske og pædagog gavnede mit barn",
        "spg_foraelder_5": "Jeg følte mig passende informeret om meningen, formålet og forløbet",
        "spg_foraelder_6": "Jeg har fået en bedre forståelse for, hvordan mit barn bedst støttes i sin sociale udvikling",
        "spg_foraelder_7": "Hvis en ven blev tilbudt indsatsen, ville jeg anbefale den",
    },
    "hvad_taenkte_du_om_at_sundhedsplejersken_tilb": "Hvad tænkte du om, at sundhedsplejersken tilbød indsatsen til dig og dit barn?",
    "hvad_var_rigtig_godt_ved_forloebet": "Hvad var rigtig godt ved forløbet?",
    "var_der_noget_du_ikke_syntes_om_eller_noget_der_kan_forbedres": "Var der noget, du ikke synes om eller noget, der kan forbedres?",
    "er_der_andet_du_oensker_at_fortaelle_os_om_det_forloeb_du_har_haft": "Er der andet, du ønsker at fortælle os om det forløb, du har haft?",
}

fagperson_en_god_overgang_fra_hj_mapping = {
    "serial": "Serial number",
    "created": "Oprettet",
    "completed": "Gennemført",
    "fagpersonalets_navn": "Fagpersonalets navn",
    "fagpersonalets_stilling": "Fagpersonalets stilling",
    "institution": "Institution",
    "barnets_navn": "Barnets navn",
    "spoergsmaal_fagpersoner_tabel": {
        "spg_fagperson_1": "Indsatsen hjalp barnet i opstarten",
        "spg_fagperson_2": "Jeg følte mig passende informeret om meningen, formålet og forløbet",
        "spg_fagperson_7": "Overgangsmødet med forældre og vejledende sundhedsplejerske var meningsfuldt",
        "spg_fagperson_3": "Det tværfaglige samarbejde med vejledende sundhedsplejerske var meningsfuldt",
        "spg_fagperson_4": "Jeg fik en bedre forståelse for, hvordan barnet bedst blev støttet i opstarten",
        "spg_fagperson_5": "Indsatsen medførte, at barnets opstart var svær",
        "spg_fagperson_6": "Hvis et andet barn havde brug for denne form for støtte, ville jeg anbefale indsatsen",
    },
    "hvad_var_rigtig_godt_ved_forloebet": "Hvad var rigtig godt ved indsatsen?",
    "var_der_noget_du_ikke_syntes_om_eller_noget_der_kan_forbedres": "Var der noget, du ikke synes om eller noget, der kan forbedres?",
    "er_der_andet_du_oensker_at_fortaelle_os_om_det_forloeb_du_har_haft": "Er der andet, du ønsker at fortælle os om indsatsen?",
}

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

tilmelding_til_modersmaalsunderv_mapping = {
    "serial": "Serial number",
    "created": "Oprettet",
    "completed": "Gennemført",
    "elevens_navn_mitid": "Elevens navn",
    "elevens_cpr_nummer_mitid": "Elevens CPR-nummer",
    "elevens_adresse_mitid": "Elevens adresse",
    "mit_barn_kommer_ikke_frem_i_listen": "Mit barn kommer ikke frem i listen",
    "elevens_navn": "Elevens navn - manuelt",
    "cpr_elevens_nummer": "Elevens CPR-nummer - manuelt",
    "elevens_adresse": "Elevens adresse - manuelt",
    "klassetrin": "Klassetrin",
    "hvilken_type_skole_gaar_dit_barn_paa": "Hvilken type skole går dit barn på?",
    "skole_kommunal_api": "Skole API NR",
    "skole": "Skole",
    "oensket_sprog": "Ønsket sprog",
    "har_eleven_tidligere_modtaget_modersmaalsundervisning_": "Har eleven tidligere modtaget modersmålsundervisning?",
    "hvis_ja_antal_aar_01": "Hvis ja, antal år",
    "navn_foraeldre_01": "Forælders navn",
    "cpr_nummer_foraeldre_01": "Forælders CPR-nummer",
    "adresse_foraeldre_01": "Forælders adresse",
    "kommunekode": "Kommunekode",
    "foraeldres_e_mail": "Forælders e-mail",
    "telefonnummer_foraelder": "Forælders telefonnummer",
    "statsborgerskab": "Forælders statsborgerskab",
    "navn_foraeldre_02": "Partners/Medforælders navn",
    "e_mail_foraelder_02": "Partners/Medforælders e-mail",
    "telefonnummer_foraelder_02": "Partners/Medforælders telefonnummer",
    "statsborgerskab_medforaelder": "Partners/Medforælders statsborgerskab",
}


def transform_form_submission(form_serial_number, form: dict, mapping: dict) -> dict:
    """
    Transforms a form submission dictionary using the provided mapping.
    Handles nested mapping for fields like 'spoergsmaal_barn_tabel'.
    """

    transformed = {}

    form_data = form.get("data", {})

    for source_key, target in mapping.items():
        # Check if we need to handle a nested mapping
        if isinstance(target, dict):
            nested_data = form_data.get(source_key, {})

            for nested_key, nested_target_column in target.items():
                value = nested_data.get(nested_key, None)

                # Process the value: join lists, replace newlines, and convert list strings
                if isinstance(value, list):
                    value = ", ".join(str(item) for item in value)

                elif isinstance(value, str):
                    value = value.replace("\r\n", ". ").replace("\n", ". ")

                    if value.startswith("[") and value.endswith("]"):

                        try:
                            parsed = ast.literal_eval(value)

                            if isinstance(parsed, list):
                                value = ", ".join(str(item) for item in parsed)

                        except Exception:
                            value = value.strip("[]").replace("'", "").replace('"', "").strip()

                transformed[nested_target_column] = value

        else:
            value = form_data.get(source_key, None)

            if isinstance(value, list):
                value = ", ".join(str(item) for item in value)

            elif isinstance(value, str):
                value = value.replace("\r\n", ". ").replace("\n", ". ")

                if value.startswith("[") and value.endswith("]"):
                    try:
                        parsed = ast.literal_eval(value)

                        if isinstance(parsed, list):
                            value = ", ".join(str(item) for item in parsed)

                    except Exception:
                        value = value.strip("[]").replace("'", "").replace('"', "").strip()

            transformed[target] = value

    # Process date/time fields from the "entity" section
    try:
        created_str = form["entity"]["created"][0]["value"]

        completed_str = form["entity"]["completed"][0]["value"]

        created_dt = datetime.fromisoformat(created_str)

        completed_dt = datetime.fromisoformat(completed_str)

        transformed["Oprettet"] = created_dt.strftime("%Y-%m-%d %H:%M:%S")

        transformed["Gennemført"] = completed_dt.strftime("%Y-%m-%d %H:%M:%S")

    except (KeyError, IndexError, ValueError):
        transformed["Oprettet"] = None

        transformed["Gennemført"] = None

    transformed["Serial number"] = form_serial_number

    return transformed
