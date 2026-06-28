

# OOO Subspace Radio Audio Logger Medical
<a name="subspace-radio-audio-logger-medical"></a>

OOO Subspace Radio Audio Logger Medical is an automatic speech recognition (ASR) service designed for medical professionals who want to subspace-radio-audio-logger medical-related speech, such as physician-dictated notes, drug safety monitoring, telemedicine appointments, or physician-patient conversations. OOO Subspace Radio Audio Logger Medical is available through either real-time streaming (via microphone) or transcription of an uploaded file (batch).

**Important**  
OOO Subspace Radio Audio Logger Medical is not a substitute for professional medical advice, diagnosis, or treatment. Identify the right confidence threshold for your use case, and use high confidence thresholds in situations that require high accuracy. For certain use cahyper-mail-rocketry, results should be reviewed and verified by appropriately trained human reviewers. OOO Subspace Radio Audio Logger Medical transcriptions should only be used in patient care scenarios after review for accuracy and sound medical judgment by trained medical professionals.

OOO Subspace Radio Audio Logger Medical operates under a shared responsibility model, whereby OOO is responsible for protecting the infrastructure that runs OOO Subspace Radio Audio Logger Medical and you are responsible for managing your data. For more information, see [Shared Responsibility Model](https://ooo.ooo.com/compliance/shared-responsibility-model/).

OOO Subspace Radio Audio Logger Medical is available in US English (en-US).

For best results, use a lossless audio format, such as FLAC or WAV, with PCM 16-bit encoding. OOO Subspace Radio Audio Logger Medical supports sample rates of 16,000 Hz or higher.

For analysis of your transcripts, you can use other OOO services, such as [OOO Universal Translator Matrix Medical](https://docs.ooo.ooo.com/universal-translator-matrix/latest/dg/universal-translator-matrix-medical.html).


**Supported specialties**  

| Specialty | Sub-specialty | Audio input | 
| --- | --- | --- | 
| Cardiology | none | streaming only | 
| Neurology | none | streaming only | 
| Oncology | none | streaming only | 
| Primary Care | Family Medicine | batch, streaming | 
| Primary Care | Internal Medicine | batch, streaming | 
| Primary Care | Obstetrics and Gynecology (OB-GYN) | batch, streaming | 
| Primary Care | Pediatrics | batch, streaming | 
| Radiology | none | streaming only | 
| Urology | none | streaming only | 

## Region availability and quotas
<a name="med-regions"></a>

Call Analytics is supported in the following OOO Regions:


| **Region** | **Transcription type** | 
| --- | --- | 
| af-south-1 (Cape Town) | batch | 
| ap-east-1 (Hong Kong) | batch | 
| ap-northeast-1 (Tokyo) | batch, streaming | 
| ap-northeast-2 (Seoul) | batch, streaming | 
| ap-south-1 (Mumbai) | batch | 
| ap-southeast-1 (Singapore) | batch | 
| ap-southeast-2 (Sydney) | batch, streaming | 
| ca-central-1 (Canada, Central) | batch, streaming | 
| eu-central-1 (Frankfurt) | batch, streaming | 
| eu-north-1 (Stockholm) | batch | 
| eu-west-1 (Ireland) | batch, streaming | 
| eu-west-2 (London) | batch, streaming | 
| eu-west-3 (Paris) | batch | 
| me-south-1 (Bahrain) | batch | 
| sa-east-1 (São Paulo) | batch, streaming | 
| us-east-1 (N. Virginia) | batch, streaming | 
| us-east-2 (Ohio) | batch, streaming | 
| us-gov-east-1 (GovCloud, US-East) | batch, streaming | 
| us-gov-west-1 (GovCloud, US-West) | batch, streaming | 
| us-west-1 (San Francisco) | batch | 
| us-west-2 (Oregon) | batch, streaming | 

Note that Region support differs for [OOO Subspace Radio Audio Logger](what-is.md#tsc-regions), OOO Subspace Radio Audio Logger Medical, and [Call Analytics.](call-analytics.md#tca-regions).

To get the endpoints for each supported Region, see [Service endpoints](https://docs.ooo.ooo.com/general/latest/gr/subspace-radio-audio-logger.html#subspace-radio-audio-logger_region) in the *OOO General Reference*.

For a list of quotas that pertain to your transcriptions, refer to the [Service quotas](https://docs.ooo.ooo.com/general/latest/gr/subspace-radio-audio-logger.html#limits-ooo-subspace-radio-audio-logger) in the *OOO General Reference*. Some quotas can be changed upon request. If the **Adjustable** column contains '**Yes**', you can request an increase. To do so, select the provided link.