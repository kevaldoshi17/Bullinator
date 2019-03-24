import requests
import cognitive_sr
import io

def recognize_speaker(wav_data):
    people = {
        '00000000-0000-0000-0000-000000000000' : 'No Match',
        'f15d5e70-4943-49e5-ba33-ff702253a3c8' : 'Safin',
        '02454ffc-7703-4029-9159-2418cf489b36' : 'Akash',
        'f304c2d8-86a1-481f-bef5-36bc78c13708' : 'Keval',
        '5579c474-3c9e-4bdd-b1a6-9480c3d1366a' : 'Yung Nav'
    }
    subscription_key = 'c16fe0be8b3c4b2eaccdfe3fd2e306b4'

    # Create a new profile
    speech_identification = cognitive_sr.SpeechIdentification(subscription_key)
    # result = speech_identification.create_profile()
    # print(result)
    profile_id = '820b1301-cb96-4155-9f22-afc0b4d891cb'
    # Pranav - 2338f519-b782-4756-b0be-557fa731f1bf
    # Sayan - 818a16b4-8068-418a-88b5-d9f45a803e93
    # Daddy Jhosh - b468f3aa-e303-4290-95ff-68a74524900e
    # Nav - 

    profile_ids = 'f15d5e70-4943-49e5-ba33-ff702253a3c8', '02454ffc-7703-4029-9159-2418cf489b36', 'f304c2d8-86a1-481f-bef5-36bc78c13708'
    #wav_path = 'jhosh_recording.wav'
   # with io.open(wav_data, 'rb') as wav_file:
        #wav_data2 = wav_data2.read()
    # result = speech_identification.enroll_profile(profile_id, wav_data)
    # result = speech_identification.delete_profile(profile_id)
    result = speech_identification.identify_profile(profile_ids, wav_data, short_audio=True)
    # result = speech_identification.get_profile(profile_id)
    # profiles = speech_identification.get_all_profiles()
    # print(profiles)
    # print(len(profiles))
    # print("Done")
    print(result)
    if 'identifiedProfileId' in result.keys():
        x = people[result['identifiedProfileId']]
        print(x, result['confidence'])
        return "Keval" if x == "No Match" else x
    else:
        # print("Pranav Normal Default")
        return "Keval"

# recognize_speaker(None)