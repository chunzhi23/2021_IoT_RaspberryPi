# PyAudio로 wav파일 재생하기

import pyaudio
import wave

# 음성데이터를 불러올때 한번에 몇개씩 가져올지
CHUNK = 1024 # 2^10

wf = wave.open('./audios/anthem of russia.wav', 'rb')
p = pyaudio.PyAudio()

# 음성데이터 스트림 열기
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

# 음성데이터를 입력받아 출력
while data:
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()
wf.close()