from rest_framework import serializers

class ResumeJObSerializer(serializers.Serializer):
    latex_resume=serializers.CharField()
    job_description=serializers.CharField()
