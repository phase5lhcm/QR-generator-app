build:
	docker build -t qr-generator .

run:
	docker run --rm -v $(pwd)/qr_codes:/app/qr_codes qr-generator

test:
	pytest

clean:
	rm -rf qr_codes