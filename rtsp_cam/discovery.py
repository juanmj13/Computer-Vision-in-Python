from onvif import ONVIFCamera

# Config
ip = '192.168.1.108'      # Camera IP
port = 80                # HTTP Port
user = 'admin'           # Cam User
password = 'AetoArch1'  # Cam Password

try:
    # Connect to the cam
    cam = ONVIFCamera(ip, port, user, password)
    
    # Create media service
    media_service = cam.create_media_service()

    # Get cam profile
    profiles = media_service.GetProfiles()
    token = profiles[0].token

    # stream setup
    stream_setup = media_service.create_type('GetStreamUri')
    stream_setup.StreamSetup = {
        'Stream': 'RTP-Unicast',
        'Transport': {'Protocol': 'RTSP'}
    }
    stream_setup.ProfileToken = token

    # Ask for URL
    uri = media_service.GetStreamUri(stream_setup)
    
    print(f"RTSP URL DISCOVERED:\n{uri.Uri}")

except Exception as e:
    print(f"Error: {e}")
